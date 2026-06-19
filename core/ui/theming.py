"""Jinja2 template renderer + CSS injection for the PSI UI."""

from pathlib import Path
from typing import Any

from jinja2 import Environment, FileSystemLoader, select_autoescape
from markupsafe import Markup
import streamlit as st

_TEMPLATES_DIR = Path(__file__).parent / "templates"
_CSS_PATH = Path(__file__).parents[2] / "static" / "app.css"

_env = Environment(
    loader=FileSystemLoader(str(_TEMPLATES_DIR)),
    autoescape=select_autoescape(["html"]),
    keep_trailing_newline=True,
)


def render_template(name: str, **ctx: Any) -> str:
    """Render a template file from the templates/ directory."""
    return _env.get_template(name).render(**ctx)


def inject_base() -> None:
    """Inject base CSS (fonts + app styles) into the page once."""
    # Mark CSS as safe so Jinja2 autoescaping does not mangle attribute
    # selectors like [data-testid="..."] into &#34; entities (invalid CSS).
    html = render_template("base.html", css_content=Markup(_CSS_PATH.read_text()))
    st.html(html)
