"""
Traven Reports View.

Generate and export glucose reports.
"""

import streamlit as st

from components.navbar import render_navbar

from core.constants import Pages


def render() -> None:
    """
    Render the Reports page.
    """

    render_navbar(
        page=Pages.REPORTS,
        user_name="Gerald",
    )

    st.write("")

    st.title("📄 Reports")

    st.write(
        "Generate professional glucose reports for personal review "
        "or sharing with your healthcare provider."
    )

    st.divider()

    # ==========================================================
    # Report Type
    # ==========================================================

    st.subheader("Report Period")

    report_period = st.radio(
        label="Choose a reporting period",
        options=[
            "Daily",
            "Weekly",
            "Monthly",
        ],
        horizontal=True,
    )

    st.write("")

    # ==========================================================
    # Report Contents
    # ==========================================================

    st.subheader("Include")

    include_summary = st.checkbox(
        "Clinical Summary",
        value=True,
    )

    include_chart = st.checkbox(
        "Glucose Trend Chart",
        value=True,
    )

    include_statistics = st.checkbox(
        "Glucose Statistics",
        value=True,
    )

    include_story = st.checkbox(
        "AI Narrative",
        value=True,
    )

    include_risk = st.checkbox(
        "Risk Assessment",
        value=True,
    )

    include_recommendations = st.checkbox(
        "Recommendations",
        value=True,
    )

    st.write("")

    st.divider()

    # ==========================================================
    # Preview
    # ==========================================================

    st.subheader("Report Preview")

    with st.container(border=True):

        st.markdown(f"**Period:** {report_period}")

        st.markdown("### Included Sections")

        if include_summary:
            st.markdown("✅ Clinical Summary")

        if include_chart:
            st.markdown("✅ Glucose Trend")

        if include_statistics:
            st.markdown("✅ Glucose Statistics")

        if include_story:
            st.markdown("✅ AI Narrative")

        if include_risk:
            st.markdown("✅ Risk Assessment")

        if include_recommendations:
            st.markdown("✅ Recommendations")

    st.write("")

    # ==========================================================
    # Export
    # ==========================================================

    st.subheader("Export")

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "📄 Export PDF",
            use_container_width=True,
        ):
            st.info(
                "PDF export will be connected in the next milestone."
            )

    with col2:

        if st.button(
            "📊 Export CSV",
            use_container_width=True,
        ):
            st.info(
                "CSV export will be connected in the next milestone."
            )

    st.write("")

    # ==========================================================
    # History
    # ==========================================================

    st.subheader("Recent Reports")

    st.info(
        "No reports have been generated yet."
    )


