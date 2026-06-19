"""Pure PSI (Photo Severity Index) damage-assessment logic.

No UI / Colab dependencies. All functions operate on numpy arrays so they
are unit-testable and reusable by any frontend.
Input images are expected as RGB numpy arrays (Streamlit / PIL convention).
"""

import time
from dataclasses import dataclass

import cv2
import numpy as np

MIN_CONTOUR_AREA = 100
ADAPTIVE_BLOCK_SIZE = 11
ADAPTIVE_C = 2
ROI_BOX_COLOR = (0, 255, 0)  # green, RGB
MASK_COLOR = (255, 0, 0)  # red, RGB
MASK_ALPHA = 0.2

SEVERITY_COLORS = {
    0: "#22c55e",  # green   — minimal
    1: "#eab308",  # yellow  — light
    2: "#f97316",  # orange  — moderate
    3: "#ef4444",  # red     — severe
    4: "#991b1b",  # dark red — very severe
}

# (inclusive upper bound on damage %, psi_index, category)
SEVERITY_RUBRIC = [
    (20.0, 0, "Minimal damage"),
    (40.0, 1, "Light damage"),
    (60.0, 2, "Moderate damage"),
    (80.0, 3, "Severe damage"),
    (float("inf"), 4, "Very severe damage"),
]


@dataclass
class PSIResult:
    damage_pct: float
    psi_index: int
    category: str
    runtime: float
    original: np.ndarray  # RGB
    roi: np.ndarray  # RGB, green bounding boxes
    masked: np.ndarray  # RGB, red alpha-blend overlay


def classify(damage_pct: float) -> tuple[int, str]:
    """Map a damage percentage to (psi_index, category) via the rubric."""
    for upper, idx, cat in SEVERITY_RUBRIC:
        if damage_pct <= upper:
            return idx, cat


def calculate_psi(image_rgb: np.ndarray | None) -> PSIResult:
    """Run the full PSI pipeline on an RGB image and return a PSIResult."""
    if image_rgb is None or not isinstance(image_rgb, np.ndarray):
        raise ValueError("calculate_psi expects a non-empty numpy image array")
    if image_rgb.ndim != 3 or image_rgb.shape[2] != 3:
        raise ValueError("calculate_psi expects an RGB image (H, W, 3)")

    start = time.perf_counter()

    gray = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)

    binary = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV,
        ADAPTIVE_BLOCK_SIZE,
        ADAPTIVE_C,
    )

    contours, _ = cv2.findContours(
        binary,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE,
    )
    valid = [c for c in contours if cv2.contourArea(c) > MIN_CONTOUR_AREA]
    damaged_area = sum(cv2.contourArea(c) for c in valid)

    height, width = gray.shape
    total_area = height * width
    damage_pct = (damaged_area / total_area) * 100 if total_area else 0.0

    psi_index, category = classify(damage_pct)

    roi = image_rgb.copy()
    for c in valid:
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(roi, (x, y), (x + w, y + h), ROI_BOX_COLOR, 2)

    mask = np.zeros_like(image_rgb)
    cv2.drawContours(mask, valid, -1, MASK_COLOR, -1)
    masked = cv2.addWeighted(image_rgb, 1.0 - MASK_ALPHA, mask, MASK_ALPHA, 0)

    runtime = time.perf_counter() - start

    return PSIResult(
        damage_pct=round(damage_pct, 2),
        psi_index=psi_index,
        category=category,
        runtime=round(runtime, 3),
        original=image_rgb,
        roi=roi,
        masked=masked,
    )
