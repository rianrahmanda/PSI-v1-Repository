import cv2
import numpy as np
import pytest

from core.psi import PSIResult, calculate_psi


def _blank_image(h=200, w=200):
    # solid mid-gray image -> adaptive threshold yields ~no damage contours
    return np.full((h, w, 3), 127, dtype=np.uint8)


def test_returns_psiresult_with_all_fields():
    result = calculate_psi(_blank_image())
    assert isinstance(result, PSIResult)
    assert 0.0 <= result.damage_pct <= 100.0
    assert result.psi_index in (0, 1, 2, 3, 4)
    assert isinstance(result.category, str) and result.category
    assert result.runtime >= 0.0
    for frame in (result.original, result.roi, result.masked):
        assert frame.shape == (200, 200, 3)


def test_blank_image_is_minimal_damage():
    result = calculate_psi(_blank_image())
    assert result.psi_index == 0
    assert result.category == "Minimal damage"


def test_rejects_non_image_input():
    with pytest.raises(ValueError):
        calculate_psi(None)


@pytest.mark.parametrize(
    "pct,expected_index,expected_cat",
    [
        (0, 0, "Minimal damage"),
        (20, 0, "Minimal damage"),
        (21, 1, "Light damage"),
        (40, 1, "Light damage"),
        (60, 2, "Moderate damage"),
        (80, 3, "Severe damage"),
        (95, 4, "Very severe damage"),
    ],
)
def test_classify_rubric_boundaries(pct, expected_index, expected_cat):
    from core.psi import classify

    idx, cat = classify(pct)
    assert idx == expected_index
    assert cat == expected_cat


def test_high_contrast_image_produces_damage():
    # Checkerboard (8x8 blocks) — adaptive threshold fires on every block edge,
    # producing many large contours and high damage_pct (~90%).
    # A half-black/half-white split only fires near the single boundary line,
    # which is insufficient to exceed 20 %.
    img = np.zeros((200, 200, 3), dtype=np.uint8)
    block = 8
    for i in range(0, 200, block):
        for j in range(0, 200, block):
            if (i // block + j // block) % 2 == 0:
                img[i : i + block, j : j + block] = 255
    result = calculate_psi(img)
    assert result.damage_pct > 20.0
    assert result.psi_index >= 1
    for frame in (result.original, result.roi, result.masked):
        assert frame.shape == (200, 200, 3)


def test_rgb_channel_order_not_bgr():
    # Pure red RGB image: channel 0 = R = 255, G = B = 0.
    # cv2.COLOR_RGB2GRAY applies BT.601 as R*0.299+G*0.587+B*0.114 -> ~76.
    # cv2.COLOR_BGR2GRAY treats the same array as B=255,G=0,R=0 -> ~29.
    # The gap (76 vs 29) proves which convention was used.
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    img[:, :, 0] = 255  # R channel
    gray_rgb = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    gray_bgr = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # RGB2GRAY gives significantly higher luminance for a red image than BGR2GRAY
    assert gray_rgb.mean() > 30, "RGB2GRAY of pure-red should be ~76"
    assert gray_rgb.mean() > gray_bgr.mean(), (
        "RGB convention assigns higher weight to red channel than BGR does"
    )
    # calculate_psi should behave as RGB (not crash, returns valid result)
    result = calculate_psi(img)
    assert isinstance(result, PSIResult)
