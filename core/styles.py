"""
CSS loader for TravenHealth.
"""

from pathlib import Path

import streamlit as st


def load_css():
    """Load all CSS files from assets/css."""

    css_dir = Path("assets/css")

    css_content = ""

    for css_file in sorted(css_dir.glob("*.css")):
        css_content += css_file.read_text(
            encoding="utf-8"
        )
        css_content += "\n"

    st.markdown(
        f"<style>{css_content}</style>",
        unsafe_allow_html=True,
    )
