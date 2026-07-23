"""
Glucose View.
"""

import streamlit as st
from components import render_page_header

from components.stat_grid import render_stat_grid


render_stat_grid(

    stats={

        "Average": "112 mg/dL",

        "Maximum": "168 mg/dL",

        "Minimum": "82 mg/dL",

        "Time in Range": "84%",

        "GMI": "6.1%",

        "CV": "27%",

        "Standard Deviation": "31 mg/dL",

        "Sensor Age": "9 days",

    },

    columns=2,

)


"""
def render():

    render_page_header(

        title="Glucose",

        subtitle="Explore your glucose patterns.",

        icon="🩸",

    )

"""
