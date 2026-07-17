"""
Traven Analytics - Pattern Detection

Detect recurring glucose behaviours and clinically
important events.

Responsibilities
----------------
✓ Meal spikes
✓ Overnight stability
✓ Hypoglycaemia
✓ Hyperglycaemia
✓ Rapid rises
✓ Rapid falls

This module does NOT:
---------------------
✗ Generate AI explanations
✗ Produce recommendations
✗ Calculate Time in Range
"""

from datetime import timedelta



# =======================================
# Helper function to extract glucose data
# =======================================

def glucose_values(readings):
    """
    Return glucose values only.
    """

    return [
        r["glucose"]
        for r in readings
    ]


# ==========================
# Detect rapid glucose rise
# ==========================

def detect_rapid_rise(
    readings,
    threshold=40,
):
    """
    Detect large glucose increases between
    consecutive readings.
    """

    events = []

    for previous, current in zip(
        readings,
        readings[1:],
    ):

        change = (
            current["glucose"]
            - previous["glucose"]
        )

        if change >= threshold:

            events.append({

                "timestamp":
                    current["timestamp"],

                "pattern":
                    "rapid_rise",

                "change":
                    change,

                "severity":
                    "warning",

            })

    return events

# ===================================
# Detect rapid fall in glucose levels
# ===================================

def detect_rapid_fall(
    readings,
    threshold=40,
):
    """
    Detect rapid glucose decreases.
    """

    events = []

    for previous, current in zip(
        readings,
        readings[1:],
    ):

        change = (
            previous["glucose"]
            - current["glucose"]
        )

        if change >= threshold:

            events.append({

                "timestamp":
                    current["timestamp"],

                "pattern":
                    "rapid_fall",

                "change":
                    change,

                "severity":
                    "warning",

            })

    return events


# ===================
# Detect Hypoglycemia
# ===================

def detect_hypoglycaemia(
    readings,
):
    """
    Detect glucose below 70 mg/dL.
    """

    events = []

    for reading in readings:

        if reading["glucose"] < 70:

            events.append({

                "timestamp":
                    reading["timestamp"],

                "pattern":
                    "hypoglycaemia",

                "glucose":
                    reading["glucose"],

                "severity":
                    "critical",

            })

    return events

# =============
# Hyperglycemia
# =============

def detect_hyperglycaemia(
    readings,
):
    """
    Detect glucose above 180 mg/dL.
    """

    events = []

    for reading in readings:

        if reading["glucose"] > 180:

            events.append({

                "timestamp":
                    reading["timestamp"],

                "pattern":
                    "hyperglycaemia",

                "glucose":
                    reading["glucose"],

                "severity":
                    "warning",

            })

    return events

# ===================
# Overnight Stability
# ===================

def detect_overnight_stability(
    readings,
):
    """
    Check whether overnight glucose remained
    within target range.
    """

    overnight = [

        r

        for r in readings

        if 0 <= r["timestamp"].hour <= 6

    ]

    if not overnight:

        return None

    stable = all(

        70 <= r["glucose"] <= 180

        for r in overnight

    )

    return {

        "pattern":
            "overnight",

        "stable":
            stable,

        "severity":
            "normal",

    }


# ===================
# Summary of Readings
# ===================

def summary(
    readings,
):
    """
    Run every pattern detector.
    """

    return {

        "rapid_rises":
            detect_rapid_rise(readings),

        "rapid_falls":
            detect_rapid_fall(readings),

        "hypoglycaemia":
            detect_hypoglycaemia(readings),

        "hyperglycaemia":
            detect_hyperglycaemia(readings),

        "overnight":
            detect_overnight_stability(readings),

    }
