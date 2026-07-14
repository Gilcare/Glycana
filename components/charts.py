"""
Traven Chart Components.

Reusable Plotly charts used throughout the platform.


Responsibility of charts.py

It should:

✅ Create glucose visualizations
✅ Apply Traven styling
✅ Accept prepared data

It should NOT:

❌ Calculate glucose averages
❌ Query CGM devices
❌ Process raw sensor packets


#  ===========================
#  UI Improvements for v.0.2.0
#  ============================
   Healthcare charts need clinical context.
   Eventually, the glucose chart should include:
   > meal markers 🍽️
   > medication markers 💊
   > exercise markers 🚶
   > AI detected events 🧠
   ============================
"""


import plotly.graph_objects as go
import streamlit as st

from core.theme import (
    PRIMARY,
    ACCENT,
    LIGHT,
    BORDER,
)



# ==========================================================
# Glucose Trend Chart
# ==========================================================


def glucose_chart(
    timestamps,
    glucose_values,
    target_low=70,
    target_high=180,
):
    """
    Display interactive glucose trend chart.

    Parameters
    ----------
    timestamps:
        List of datetime values.

    glucose_values:
        List of glucose readings.

    target_low:
        Lower target glucose boundary.

    target_high:
        Upper target glucose boundary.
    """


    fig = go.Figure()


    # Glucose line

    fig.add_trace(
        go.Scatter(
            x=timestamps,
            y=glucose_values,

            mode="lines",

            name="Glucose",

            line=dict(
                color=PRIMARY,
                width=3,
            ),

        )
    )


    # Target range

    fig.add_hrect(

        y0=target_low,

        y1=target_high,

        fillcolor=LIGHT,

        opacity=0.4,

        line_width=0,

    )


    fig.update_layout(

        height=350,

        margin=dict(
            l=20,
            r=20,
            t=20,
            b=20,
        ),


        paper_bgcolor="white",

        plot_bgcolor="white",


        xaxis=dict(

            showgrid=False,

        ),


        yaxis=dict(

            title="Glucose",

            gridcolor=BORDER,

        ),


        showlegend=False,

    )


    st.plotly_chart(
        fig,
        use_container_width=True,
    )



# ==========================================================
# Time In Range Chart
# ==========================================================


def time_in_range_chart(
    in_range,
    high,
    low,
):
    """
    Display glucose distribution.
    """


    fig = go.Figure(

        data=[

            go.Pie(

                labels=[
                    "In Range",
                    "High",
                    "Low",
                ],

                values=[
                    in_range,
                    high,
                    low,
                ],

                hole=0.65,

            )

        ]

    )


    fig.update_layout(

        height=300,

        showlegend=True,

        margin=dict(
            t=10,
            b=10,
        ),

    )


    st.plotly_chart(
        fig,
        use_container_width=True,
    )
