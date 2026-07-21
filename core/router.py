"""
Traven Router.

Handles page navigation.
"""

from core.constants import Pages

from views import (
    dashboard,
    glucose,
    insights,
    reports,
    settings,
)


def render_page(page: Pages) -> None:
    """
    Render the selected page.
    """

    routes = {

        Pages.DASHBOARD: dashboard.render,

        Pages.GLUCOSE: glucose.render,

        Pages.INSIGHTS: insights.render,

        Pages.REPORTS: reports.render,

        Pages.SETTINGS: settings.render,

    }

    routes.get(
        page,
        dashboard.render,
    )()
