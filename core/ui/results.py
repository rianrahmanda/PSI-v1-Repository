"""Results components — KPI metric cards + 3-panel image view."""

import streamlit as st

from core.psi import SEVERITY_COLORS, PSIResult
from core.ui.theming import render_template


def _inject_severity_color(psi_index: int) -> None:
    color = SEVERITY_COLORS[psi_index]
    st.html(render_template("severity.html", color=color))


def render_metrics(result: PSIResult) -> None:
    """Metrics row: 4 KPI cards + severity-colored progress bar."""
    _inject_severity_color(result.psi_index)

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("PSI INDEX", f"{result.psi_index}")
    c2.metric("CATEGORY", result.category)
    c3.metric("DAMAGE", f"{result.damage_pct:.2f}%")
    c4.metric("RUNTIME", f"{result.runtime:.3f}s")
    st.progress(min(result.damage_pct / 100, 1.0))


def render_image_panels(result: PSIResult) -> None:
    """Three-column image comparison: original / ROI boxes / damage mask."""
    p1, p2, p3 = st.columns(3)
    p1.image(result.original, caption="Original", width="stretch")
    p2.image(result.roi, caption="ROI bounding boxes", width="stretch")
    p3.image(result.masked, caption="Damage mask", width="stretch")
