"""
TravenHealth Application Router.

Controls navigation between application views.
"""
import streamlit as st

from core.constants import Pages

from views import dashboard
from views import glucose
from views import reports
from views import settings
from views import insights



def route(page: Pages):
    """
    Route the user to the selected page.

    Parameters
    ----------
    page:
        Selected application page.
    """


    if page == Pages.DASHBOARD:

        dashboard.render()
   

    if page == Pages.GLUCOSE:
        glucose.render()
     
    if page == Pages.INSIGHTS:
        insights.render()

    if page == Pages.REPORTS:
        reports.render()

    if page == Page.SETTINGS:
        settings.render()
        
    else:
        st.header("🔌404 !")
        
