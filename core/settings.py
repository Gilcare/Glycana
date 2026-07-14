"""
Application configuration.
Controls how the TravenHealth application behaves, e.g:

 > Should analytics be turned on?

 >Should AI insights be available? etc

These belong here.
"""

APP_NAME = "TravenHealth"

APP_VERSION = "0.1.0"

PAGE_TITLE = "TravenHealth"

PAGE_ICON = "🌊"

LAYOUT = "wide"

SIDEBAR_STATE = "expanded"

MAX_CONTENT_WIDTH = 1400

ENABLE_ANIMATIONS = True

ENABLE_DEMO_MODE = True




# ==========================================================
# Development Settings
# ==========================================================

# Used while building the application.
# Disable before production launch.

DEMO_MODE = True


# ==========================================================
# Feature Flags
# ==========================================================

ENABLE_AI_INSIGHTS = True

ENABLE_REPORTS = True

ENABLE_CGM_CONNECTION = False

ENABLE_NOTIFICATIONS = False


# ==========================================================
# Data Settings
# ==========================================================

DEFAULT_TIMEZONE = "Africa/Lagos"

DATE_FORMAT = "%d %b %Y"


# ==========================================================
# Limits
# ==========================================================

MAX_RECENT_READINGS = 50

MAX_INSIGHT_LENGTH = 250
