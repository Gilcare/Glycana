"""
TravenHealth Application Router.

Controls navigation between application views.
"""


from core.constants import Pages

from views import dashboard
from views import glucose



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
   

    elif:

        page == Pages.GLUCOSE:
            glucose.render()
     
    
    else:

        # Temporary placeholder
        # until other pages exist
        insights_render()
        reports_render()
        settings_render()

        """
        raise NotImplementedError(
            f"{page.value} page is not available yet."
        )
        """
