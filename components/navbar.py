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
        
    st.markdown(
    f"""
    <div style="
        display:flex;
        justify-content:space-between;
        align-items:center;
        background:white;
        padding:20px;
        border-radius:16px;
        border:1px solid #d8dde2;
    ">

        <div>

            <h2 style="
                color:#042754;
                margin:0;
            ">
                {greeting}, {user_name} 👋
            </h2>


            <p style="
                color:#2788b2;
                margin:5px 0 0 0;
            ">
                {page.value}
            </p>

        </div>


        <div style="
            color:#2788b2;
            font-weight:600;
        ">

            🟢 CGM Ready

        </div>

    </div>
    """,
    unsafe_allow_html=True,
)




name = "Gerald"

st.markdown(
    f"""
    <div style="background:#042754;color:white;padding:20px;">
        Hello {name}
    </div>
    """,
    unsafe_allow_html=True,
)
