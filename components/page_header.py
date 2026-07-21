"""
Reusable page header component.
"""

import streamlit as st


def render_page_header(
    title: str,
    subtitle: str = "",
    icon: str = "",
) -> None:
    """
    Render a consistent page header.
    """

    if icon:
        title = f"{icon} {title}"

    st.title(title)

    if subtitle:
        st.caption(subtitle)

    st.divider()
