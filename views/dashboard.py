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
from components.charts import (
    glucose_chart,
    time_in_range_chart,
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


    # ------------------------------------------------------
    # Charts
    # ------------------------------------------------------

    left, right = st.columns(
        [2,1]
    )


    with left:

        glucose_chart(

            timestamps=[
                "08:00",
                "10:00",
                "12:00",
                "14:00",
                "16:00",
            ],

            glucose_values=[
                95,
                120,
                165,
                130,
                108,
            ],

        )


    with right:

        time_in_range_chart(

            in_range=82,

            high=14,

            low=4,

        )



    st.write("")


    # ------------------------------------------------------
    # Timeline
    # ------------------------------------------------------
    """
    st.subheader(
        "Today's Journey"
    )


    events = [

        {
            "time": "08:00",
            "title": "Breakfast",
            "description":
                "Glucose increased gradually",
            "status": "normal",
        },


        {
            "time": "12:30",
            "title": "Lunch Response",
            "description":
                "Moderate glucose spike detected",
            "status": "warning",
        },


        {
            "time": "15:00",
            "title": "Returned to Range",
            "description":
                "Glucose stabilized",
            "status": "normal",
        },

    ]
    """

    render_timeline(events)



    st.write("")


    
