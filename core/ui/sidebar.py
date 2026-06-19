"""Sidebar component — passes data to templates/sidebar.html."""

import streamlit as st

from core.psi import SEVERITY_COLORS, SEVERITY_RUBRIC
from core.ui.theming import render_template

_PIPELINE_TAGS = ["Adaptive Threshold", "Contour Analysis", "Gaussian Segmentation"]


def render_sidebar() -> None:
    rubric_rows = [
        (
            f"≤{int(upper)}" if upper != float("inf") else "≤100",
            psi,
            category,
            SEVERITY_COLORS[psi],
        )
        for upper, psi, category in SEVERITY_RUBRIC
    ]
    html = render_template(
        "sidebar.html",
        pipeline_tags=_PIPELINE_TAGS,
        rubric_rows=rubric_rows,
    )
    with st.sidebar:
        st.html(html)
