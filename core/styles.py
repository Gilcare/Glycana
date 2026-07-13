"""
Global CSS for the TravenHealth app platform.

This module is responsible for injecting all custom styling used
throughout the application.

The goal is to override Streamlit's default appearance and create
a clean, premium interface that matches the TravenHealth brand.

Usage
-----
from core.styles import load_css

load_css()
"""

import streamlit as st

from core.theme import (
    PRIMARY,
    ACCENT,
    SECONDARY,
    BACKGROUND,
    BORDER,
    LIGHT,
    TEXT_PRIMARY,
    TEXT_SECONDARY,
    CARD_BACKGROUND,
    CARD_BORDER,
    RADIUS_SMALL,
    RADIUS_MEDIUM,
    RADIUS_LARGE,
    SHADOW_LIGHT,
)


def load_css() -> None:
    """Inject the global TravenHealth stylesheet."""

    st.markdown(
        f"""
<style>

/* ==========================================================
   Google Font
========================================================== */

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');


/* ==========================================================
   Global
========================================================== */

html, body, [class*="css"] {{
    font-family: 'Inter', sans-serif;
}}

body {{
    background: {BACKGROUND};
    color: {TEXT_PRIMARY};
}}


/* ==========================================================
   Main App
========================================================== */

.block-container {{
    padding-top: 2rem;
    padding-bottom: 2rem;
    padding-left: 3rem;
    padding-right: 3rem;
    max-width: 1400px;
}}


/* ==========================================================
   Sidebar
========================================================== */

section[data-testid="stSidebar"] {{
    background: white;
    border-right: 1px solid {BORDER};
}}

section[data-testid="stSidebar"] * {{
    color: {PRIMARY};
}}


/* ==========================================================
   Buttons
========================================================== */

.stButton > button {{

    background: {PRIMARY};

    color: white;

    border: none;

    border-radius: {RADIUS_MEDIUM};

    padding: .7rem 1.2rem;

    font-weight: 600;

    transition: all .2s ease;
}}

.stButton > button:hover {{

    background: {SECONDARY};

    transform: translateY(-1px);
}}


/* ==========================================================
   Inputs
========================================================== */

.stTextInput input,
.stNumberInput input,
.stDateInput input,
textarea {{

    border-radius: {RADIUS_SMALL};

    border: 1px solid {CARD_BORDER};
}}


/* ==========================================================
   Cards
========================================================== */

.travenhealth-card {{

    background: {CARD_BACKGROUND};

    border: 1px solid {CARD_BORDER};

    border-radius: {RADIUS_LARGE};

    padding: 24px;

    box-shadow: {SHADOW_LIGHT};

    margin-bottom: 1rem;
}}


/* ==========================================================
   Card Titles
========================================================== */

.travenhealth-card-title {{

    color: {PRIMARY};

    font-size: 1rem;

    font-weight: 600;

    margin-bottom: .6rem;
}}


/* ==========================================================
   Metric Values
========================================================== */

.travenhealth-metric {{

    color: {PRIMARY};

    font-size: 2rem;

    font-weight: 700;
}}


/* ==========================================================
   Secondary Text
========================================================== */

.travenhealth-muted {{

    color: {TEXT_SECONDARY};
}}


/* ==========================================================
   Story Card
========================================================== */

.story-card {{

    background: {LIGHT};

    border-radius: {RADIUS_LARGE};

    border: none;

    padding: 30px;
}}


/* ==========================================================
   Horizontal Rule
========================================================== */

hr {{

    border: none;

    border-top: 1px solid {BORDER};

}}

</style>
""",
        unsafe_allow_html=True,
    )
