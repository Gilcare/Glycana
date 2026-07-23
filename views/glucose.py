"""
Glucose View.
"""

import streamlit as st
from components import render_page_header


def render():

    render_page_header(

        title="Glucose",

        subtitle="Explore your glucose patterns.",

        icon="🩸",

    )

