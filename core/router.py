"""
TravenHealth Application Router.

Controls navigation between application views.
"""


from core.constants import Pages

from views import dashboard



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


    else:

        # Temporary placeholder
        # until other pages exist

        raise NotImplementedError(
            f"{page.value} page is not available yet."
        )
