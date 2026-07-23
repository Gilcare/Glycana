
#from components import render_page_header
"""
Traven Glucose View.

Detailed glucose analysis page.
"""

import streamlit as st

from components.navbar import render_navbar
from components.charts import glucose_chart
from components.timeline import render_timeline
from components.cards import (
    metric_card,
    sensor_card,
)

from core.constants import Pages


def render() -> None:
    """
    Render the Glucose page.
    """

    render_navbar(
        page=Pages.GLUCOSE,
        user_name="Gerald",
    )

    st.write("")

    # --------------------------------------------------
    # Time Range
    # --------------------------------------------------

    period = st.segmented_control(
        "Time Range",
        options=[
            "Today",
            "7 Days",
            "14 Days",
            "30 Days",
        ],
        default="Today",
    )

    st.write(f"Viewing **{period}** glucose data.")

    st.write("")

    # --------------------------------------------------
    # Summary Metrics
    # --------------------------------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        metric_card(
            label="Current",
            value="108 mg/dL",
            description="Current Reading",
            icon="🩸",
        )

    with col2:
        metric_card(
            label="Average",
            value="112 mg/dL",
            description="Average",
            icon="📊",
        )

    with col3:
        metric_card(
            label="Highest",
            value="168 mg/dL",
            description="Today's Peak",
            icon="📈",
        )

    with col4:
        metric_card(
            label="Lowest",
            value="82 mg/dL",
            description="Today's Lowest",
            icon="📉",
        )

    st.write("")

    # --------------------------------------------------
    # Glucose Chart
    # --------------------------------------------------

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

    st.write("")

    # --------------------------------------------------
    # Events + Sensor
    # --------------------------------------------------

    left, right = st.columns([2, 1])

    with left:

        st.subheader("Detected Events")

        events = [

            {
                "time": "08:00",
                "title": "Breakfast",
                "description": "Glucose increased gradually.",
                "status": "normal",
            },

            {
                "time": "12:30",
                "title": "Lunch Spike",
                "description": "Moderate rise detected.",
                "status": "warning",
            },

            {
                "time": "15:00",
                "title": "Returned to Range",
                "description": "Glucose stabilized.",
                "status": "normal",
            },

        ]

        render_timeline(events)

    with right:

        st.subheader("Sensor")

        sensor_card(
            device_name="Aidex-X",
            status="Connected",
            connected=True,
        )
