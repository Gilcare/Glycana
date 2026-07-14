import streamlit as st


from core.settings import (
    PAGE_TITLE,
    PAGE_ICON,
    LAYOUT,
    SIDEBAR_STATE,
)


from core.styles import load_styles


from components.sidebar import render_sidebar


from core.constants import Pages


from core.router import route



# ==========================================================
# Streamlit Configuration
# ==========================================================


st.set_page_config(

    page_title=PAGE_TITLE,

    page_icon=PAGE_ICON,

    layout=LAYOUT,

    initial_sidebar_state=SIDEBAR_STATE,

)



# ==========================================================
# Load Styling
# ==========================================================

load_styles()


st.markdown(
    """
    <div style="
        background:#042754;
        color:white;
        padding:20px;
        border-radius:15px;
    ">
        Traven CSS Test
    </div>
    """,
    unsafe_allow_html=True,
)


# ==========================================================
# Default Page
# ==========================================================

if "page" not in st.session_state:

    st.session_state.page = Pages.DASHBOARD



# ==========================================================
# Navigation
# ==========================================================


selected_page = render_sidebar(

    current_page=st.session_state.page

)


st.session_state.page = selected_page



# ==========================================================
# Render Page
# ==========================================================


route(

    st.session_state.page

)
