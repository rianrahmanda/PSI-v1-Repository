"""Upload zone component."""

import streamlit as st


def render_upload_zone():
    """Render styled upload zone; return uploaded file or None."""
    return st.file_uploader(
        "upload",
        type=["jpg", "jpeg", "png", "bmp", "webp"],
        label_visibility="collapsed",
    )
