"""
Reports View.
"""

import streamlit as st
from components import render_page_header


def render():

    render_page_header(

        title="Reports",

        subtitle="Generate and export reports.",

        icon="📄",

    )
