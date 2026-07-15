"""
TravenHealth Style Loader.

Loads custom CSS files into Streamlit.
"""

from pathlib import Path

import streamlit as st



def load_styles():
    """
    Load all Traven CSS files.
    """

    css_path = Path("assets/css")


    css_files = [

        "base.css",
        "typography.css",
        "layout.css",
        "cards.css",
        "buttons.css",
        "forms.css",
        "navigation.css",

    ]


    css_content = ""


    for file in css_files:

        file_path = css_path / file


        if file_path.exists():

            css_content += file_path.read_text()


    st.markdown(

        f"""
        <style>
        {css_content}
        </style>
        """,

        unsafe_allow_html=True,

    )



