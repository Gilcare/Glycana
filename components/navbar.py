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
    background:white;
    padding:20px;
    ">
    
    <h2 style="
    color:{PRIMARY};
    ">
    {greeting}, {user_name} 👋
    </h2>
    
    <p>
    {page.value}
    </p>

    <div>
    🟢 CGM Ready
    </div>
    
    </div>
    """
    
    
    st.markdown(
        navbar_html,
        unsafe_allow_html=True,
    )
