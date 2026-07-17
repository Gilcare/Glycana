"""
Traven Analytics - Metrics

Calculates standard Continuous Glucose Monitoring (CGM) metrics.

Responsibilities
----------------
✓ Current glucose
✓ Average glucose
✓ Minimum glucose
✓ Maximum glucose
✓ Time In Range (TIR)
✓ Time Above Range (TAR)
✓ Time Below Range (TBR)
✓ Glucose Management Indicator (GMI)

This module does NOT:
---------------------
✗ Clean glucose data
✗ Detect patterns
✗ Generate AI insights
"""

from statistics import mean


# ==========================================================
# Clinical Thresholds (mg/dL)
# ==========================================================

LOW_THRESHOLD = 70
HIGH_THRESHOLD = 180


# ==========================================================
# Helper function for extracting glucose values
# ==========================================================

def glucose_values(readings: list[dict]) -> list[float]:
    """
    Extract glucose values from CGM readings.
    """

    return [
        reading["glucose"]
        for reading in readings
    ]


# ==========================================================
# Basic Metrics
# ==========================================================

def current_glucose(readings: list[dict]) -> float | None:
    """
    Return the latest glucose value.
    """

    if not readings:
        return None

    return readings[-1]["glucose"]


def average_glucose(readings: list[dict]) -> float | None:
    """
    Calculate average glucose.
    """

    values = glucose_values(readings)

    if not values:
        return None

    return round(mean(values), 1)


def minimum_glucose(readings: list[dict]) -> float | None:
    """
    Lowest glucose reading.
    """

    values = glucose_values(readings)

    if not values:
        return None

    return min(values)


def maximum_glucose(readings: list[dict]) -> float | None:
    """
    Highest glucose reading.
    """

    values = glucose_values(readings)

    if not values:
        return None

    return max(values)


def glucose_range(readings: list[dict]) -> float | None:
    """
    Difference between maximum and minimum glucose.
    """

    values = glucose_values(readings)

    if not values:
        return None

    return max(values) - min(values)

# =====================================
# Median Glucose
# =====================================


def median_glucose(readings: list[dict]) -> float | None:
    """
    Calculate the median glucose.
    """

    values = glucose_values(readings)

    if not values:
        return None

    return round(median(values), 1)
# ==========================================================
# Time in Range
# ==========================================================

def percent_time_in_range(
    readings: list[dict],
    low: int = LOW_THRESHOLD,
    high: int = HIGH_THRESHOLD,
) -> float:
    """
    Percentage of readings within target range.
    """

    if not readings:
        return 0.0

    count = sum(
        low <= reading["glucose"] <= high
        for reading in readings
    )

    return round((count / len(readings)) * 100, 1)


def percent_time_above_range(
    readings: list[dict],
    high: int = HIGH_THRESHOLD,
) -> float:
    """
    Percentage of readings above target range.
    """

    if not readings:
        return 0.0

    count = sum(
        reading["glucose"] > high
        for reading in readings
    )

    return round((count / len(readings)) * 100, 1)


def percent_time_below_range(
    readings: list[dict],
    low: int = LOW_THRESHOLD,
) -> float:
    """
    Percentage of readings below target range.
    """

    if not readings:
        return 0.0

    count = sum(
        reading["glucose"] < low
        for reading in readings
    )

    return round((count / len(readings)) * 100, 1)


# ================================================================
# Percentage readings <54mg/dL, 54-69mg/dL, 181-250mg/dL, >250mg/dL 
# =================================================================
def time_very_low(
    readings: list[dict],
) -> float:
    """
    Percentage of readings below 54 mg/dL.
    """

    if not readings:
        return 0.0

    count = sum(
        reading["glucose"] < 54
        for reading in readings
    )

    return round((count / len(readings)) * 100, 1)

def time_low(
    readings: list[dict],
) -> float:
    """
    Percentage of readings between
    54 and 69 mg/dL.
    """

    if not readings:
        return 0.0

    count = sum(
        54 <= reading["glucose"] < 70
        for reading in readings
    )

    return round((count / len(readings)) * 100, 1)


def time_high(
    readings: list[dict],
) -> float:
    """
    Percentage of readings between
    181 and 250 mg/dL.
    """

    if not readings:
        return 0.0

    count = sum(
        180 < reading["glucose"] <= 250
        for reading in readings
    )

    return round((count / len(readings)) * 100, 1)


def time_very_high(
    readings: list[dict],
) -> float:
    """
    Percentage of readings above
    250 mg/dL.
    """

    if not readings:
        return 0.0

    count = sum(
        reading["glucose"] > 250
        for reading in readings
    )

    return round((count / len(readings)) * 100, 1)



# ==================================
# Estimate HbA1C using ADAG Equation
# ==================================

def estimated_hba1c(
    readings: list[dict],
) -> float | None:
    """
    Estimate HbA1c using the ADAG equation.

    HbA1c = (Average Glucose + 46.7) / 28.7
    """

    avg = average_glucose(readings)

    if avg is None:
        return None

    return round((avg + 46.7) / 28.7, 1)



# ==========================================================
# Glucose Management Indicator (GMI)
# ==========================================================

def glucose_management_indicator(
    readings: list[dict],
) -> float | None:
    """
    Calculate the Glucose Management Indicator (GMI).

    Formula:
        GMI = 3.31 + (0.02392 × Mean Glucose)

    Mean glucose must be in mg/dL.
    """

    avg = average_glucose(readings)

    if avg is None:
        return None

    return round(3.31 + (0.02392 * avg), 2)


# ==========================================================
# Summary
# ==========================================================

def summary(readings: list[dict]) -> dict:
    """
    Return all core glucose metrics.
    """

    return {
        "current_glucose": current_glucose(readings),
        "average_glucose": average_glucose(readings),
        "median_glucose": median_glucose(readings),
        "minimum_glucose": minimum_glucose(readings),
        "maximum_glucose": maximum_glucose(readings),
        "glucose_range": glucose_range(readings),
        
        "time_in_range": percent_time_in_range(readings),
        "time_above_range": percent_time_above_range(readings),
        "time_below_range": percent_time_below_range(readings),
        
        "time_very_low": time_very_low(readings),
        "time_low": time_low(readings),
        "time_high": time_high(readings),
        "time_very_high": time_very_high(readings),
        
        "gmi": glucose_management_indicator(readings),
        "estimated_hba1c": estimated_hba1c(readings),
    }
    
