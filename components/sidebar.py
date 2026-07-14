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


def render_sidebar(current_page: Pages) -> Pages:
    """
    Render the Traven sidebar navigation.

    Parameters
    ----------
    current_page:
        The currently active application page.

    Returns
    -------
    Pages:
        The page selected by the user.
    """

    with st.sidebar:

        # Brand
        st.markdown(
            f"""
            <div class="sidebar-brand">

                <h2 style="color:{PRIMARY};">
                    TRAVENHEALTH...replace with logo.png
                </h2>

                <p>
                    Smarter diabetes care
                </p>

            </div>
            """,
            unsafe_allow_html=True,
        )


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

        st.markdown(
            f"""
            <div class="sensor-card">

                <strong>
                    CGM Status
                </strong>

                <br>

                Not Connected

            </div>
            """,
            unsafe_allow_html=True,
        )


    return selected_page
