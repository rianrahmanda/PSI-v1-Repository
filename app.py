"""PSI Structural Damage Assessor — entry point.

Run:  streamlit run app.py
"""

import numpy as np
import streamlit as st
from PIL import Image

from core.psi import calculate_psi
from core.ui.theming import inject_base
from core.ui.results import render_image_panels, render_metrics
from core.ui.sidebar import render_sidebar
from core.ui.upload import render_upload_zone

st.set_page_config(page_title="PSI Damage Assessor", page_icon="🏗️", layout="wide")


def main() -> None:
    inject_base()
    render_sidebar()
    st.title("PSI Structural Damage Assessor")

    uploaded = render_upload_zone()
    if uploaded is None:
        return

    image_rgb = np.array(Image.open(uploaded).convert("RGB"))

    with st.spinner("Analyzing…"):
        try:
            result = calculate_psi(image_rgb)
        except ValueError as e:
            st.error(f"Analysis failed: {e}")
            return

    render_metrics(result)
    render_image_panels(result)


if __name__ == "__main__":
    main()
