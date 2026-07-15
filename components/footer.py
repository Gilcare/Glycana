"""
Traven Footer Component.

Displays lightweight application information.
"""


import streamlit as st

from core.settings import APP_NAME, APP_VERSION
from core.theme import TEXT_SECONDARY, BORDER


"""
def render_footer() -> None:
    """
    Render the application footer.
    """

    st.markdown(
        f"""
        <div class="footer">

            <div>

                <span>
                    {APP_NAME}
                </span>

                ·

                <span>
                    v{APP_VERSION}
                </span>

            </div>


            <div>

                Built for smarter diabetes care

            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )
    """
