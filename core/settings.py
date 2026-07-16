"""
Application configuration.
Controls how the TravenHealth application behaves, e.g:

 > Should analytics be turned on?

 >Should AI insights be available? etc

These belong here.
"""

APP_NAME = "Traven"

APP_VERSION = "0.1.0"

PAGE_TITLE = "Traven"

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
# Data Limits
# ==========================================================

# One day of 5-minute CGM readings
MAX_RECENT_READINGS = 288  #previously set at 50


# Maximum size of AI-generated insight cards
MAX_INSIGHT_CHARACTERS = 250
