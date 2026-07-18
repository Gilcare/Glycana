"""
Trend Analysis

Interprets analytics generated from CGM data.

Responsibilities
----------------
✓ Detect glucose stability
✓ Detect improving control
✓ Detect worsening control
✓ Detect frequent excursions
✓ Summarize today's glucose behaviour

This module does NOT:
---------------------
✗ Call LLMs
✗ Generate recommendations
✗ Assess risk
"""

from services.analytics.metrics import summary as metric_summary
from services.analytics.variability import summary as variability_summary
from services.analytics.patterns import summary as pattern_summary



def glucose_direction(readings: list[dict]) -> dict:
    """
    Determine whether glucose is rising,
    falling or stable.

    Uses the first and last readings.
    """

    if len(readings) < 2:

        return {
            "status": "unknown",
            "change": 0,
        }

    first = readings[0]["glucose"]
    last = readings[-1]["glucose"]

    change = last - first

    if change >= 20:

        status = "rising"

    elif change <= -20:

        status = "falling"

    else:

        status = "stable"

    return {

        "status": status,
        "change": change,

    }


def stability(readings: list[dict]) -> dict:
    """
    Determine overall glucose stability.
    """

    variability = variability_summary(readings)

    return {

        "status":
            variability["variability_level"],

        "score":
            variability["variability_score"],

    }


def daily_control(readings: list[dict]) -> dict:
    """
    Evaluate today's glucose control.
    """

    metrics = metric_summary(readings)

    tir = metrics["time_in_range"]

    if tir >= 80:

        status = "excellent"

    elif tir >= 70:

        status = "good"

    elif tir >= 50:

        status = "fair"

    else:

        status = "needs_attention"

    return {

        "status": status,

        "tir": tir,

    }


def excursions(readings: list[dict]) -> dict:
    """
    Count significant glucose events.
    """

    patterns = pattern_summary(readings)

    return {

        "hypoglycaemia":

            len(patterns["hypoglycaemia"]),

        "hyperglycaemia":

            len(patterns["hyperglycaemia"]),

        "rapid_rises":

            len(patterns["rapid_rises"]),

        "rapid_falls":

            len(patterns["rapid_falls"]),

    }


def summary(readings: list[dict]) -> dict:
    """
    Return interpreted glucose trends.
    """

    return {

        "direction":
            glucose_direction(readings),

        "stability":
            stability(readings),

        "daily_control":
            daily_control(readings),

        "excursions":
            excursions(readings),

    }
