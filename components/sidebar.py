"""
TravenHealth Sidebar Component.

Responsible for rendering the main application navigation.

The sidebar controls the entire application experience.


Responsibility of sidebar.py

It should:

✅ Display TravenHealth logo
✅ Display navigation options
✅ Highlight active page
✅ Return the user's selection

It should NOT:

❌ Load glucose data
❌ Query MongoDB
❌ Authenticate users
❌ Render dashboard content
"""






import streamlit as st

from core.constants import Pages
from core.theme import PRIMARY, LIGHT, BORDER


import streamlit as st

def render_sidebar(current_page: pages) -> pages:
    """
    Render the Traven sidebar navigation.
    """
    with st.sidebar:
        # 1. Display the logo as text with the specific hex color
        st.markdown(
            '<h1 style="color: #67b0e8; font-size: 2rem; margin-bottom: 0;">Traven</h1>', 
            unsafe_allow_html=True
        )
        
        # 2. Brand tagline right below
        st.caption("smarter diabetes care")
        
        
        
        # --- Rest of your sidebar navigation code ---
        st.divider()


        # Navigation

        selected_page = st.radio(
            label="Navigation",
            options=list(Pages),
            format_func=lambda page: page.value,
            index=list(Pages).index(current_page),
            label_visibility="collapsed",
        )


        st.divider()


        # Sensor status placeholder

        st.markdown("CGM Status 🟢")


    return selected_page





