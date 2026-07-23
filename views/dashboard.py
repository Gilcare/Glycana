"""
Traven Dashboard View.

Main patient overview screen.
"""


import streamlit as st

from components.navbar import render_navbar
from components.cards import (
    metric_card,
    insight_card,
    sensor_card,
)

from components.timeline import render_timeline


from core.constants import Pages



def render():
    """
    Render the Traven dashboard.
    """


    # ------------------------------------------------------
    # Header
    # ------------------------------------------------------

    render_navbar(
        page=Pages.DASHBOARD,
        user_name="Gerald",
    )


    st.write("")


    # ------------------------------------------------------
    # Top Metrics
    # ------------------------------------------------------

    col1, col2, col3, col4 = st.columns(4)

    
    
    
    with col1:

        metric_card(
            label="Current Glucose",
            value="108 mg/dL",
            description="Stable",
            icon="🩸",
        )


    with col2:

        metric_card(
            label="Time in Range",
            value="82%",
            description="Today",
            icon="🎯",
        )


    with col3:

        metric_card(
            label="Average",
            value="112 mg/dL",
            description="Last 24 hours",
            icon="📊",
        )


    with col4:

        sensor_card(
            device_name="Aidex-X",
            status="Connected",
            connected=True,
        )



    st.write("")


    # ------------------------------------------------------
    # AI Insight
    # ------------------------------------------------------

    insight_card(

        title="Today's Story",

        message=(
            "Your glucose remained stable today. "
            "A moderate rise was detected after lunch "
            "but returned to your target range."
        ),

    )


    st.write("")

    st.warning(
        "⚠️ Lunch spike detected at 12:30."
    )

    st.write("")
    
    st.info(
        "💡 Recommendation\n\n"
        "Take a 10-minute walk after lunch to reduce the post-meal glucose rise."
    )


  
