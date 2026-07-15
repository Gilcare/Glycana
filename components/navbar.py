"""
Traven Navbar Component.

Responsible for rendering the top application header.

Responsibility of navbar.py

It should:

✅ Display page title
✅ Display user greeting
✅ Show quick status information
✅ Show notification indicator (placeholder for now)

It should not:

❌ Fetch glucose readings
❌ Generate AI insights
❌ Query MongoDB
❌ Handle authentication
"""


import streamlit as st

from datetime import datetime

from core.theme import PRIMARY, SECONDARY, BORDER
from core.constants import Pages



def render_navbar(
    page: Pages,
    user_name: str = "User"
) -> None:
    """
    Render the top navigation bar.

    Parameters
    ----------
    page:
        Current active page.

    user_name:
        Name displayed in greeting.
    """

    current_time = datetime.now()

    hour = current_time.hour


    # Simple greeting logic

    if hour < 12:
        greeting = "Good morning"

    elif hour < 18:
        greeting = "Good afternoon"

    else:
        greeting = "Good evening"

    
    navbar_html = f"""
    <div style="
        display:flex;
        justify-content:space-between;
        align-items:center;
        background:white;
        border:1px solid #d8dde2;
        border-radius:18px;
        padding:20px 24px;
        margin-bottom:24px;
    ">

        <div>

            <h2 style="
                margin:0;
                color:#042754;
                font-size:28px;
            ">
                {greeting}, {user_name} 👋
            </h2>

            <p style="
                margin-top:6px;
                color:#2788b2;
                font-size:16px;
            ">
                {page.value}
            </p>

        </div>

        <div style="
            background:#cae8ff;
            color:#042754;
            padding:8px 14px;
            border-radius:999px;
            font-weight:600;
        ">
            🟢 CGM Ready
        </div>

    </div>
    """

    st.markdown(
        navbar_html,
        unsafe_allow_html=True,
    )
