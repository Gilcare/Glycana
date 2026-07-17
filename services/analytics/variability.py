"""
Traven Analytics - Variability

Calculates glucose variability metrics from Continuous Glucose
Monitoring (CGM) data.

Responsibilities
----------------
✓ Standard Deviation (SD)
✓ Coefficient of Variation (CV)
✓ Glucose Variability Score
✓ Variability Classification

This module does NOT:
---------------------
✗ Calculate Time in Range
✗ Detect glucose patterns
✗ Generate AI insights
"""

from statistics import mean, stdev


# ==========================================================
# Helper
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
# Standard Deviation
# ==========================================================

def standard_deviation(
    readings: list[dict],
) -> float | None:
    """
    Calculate glucose standard deviation.
    """

    values = glucose_values(readings)

    if len(values) < 2:
        return None

    return round(stdev(values), 1)


# ==========================================================
# Coefficient of Variation
# ==========================================================

def coefficient_of_variation(
    readings: list[dict],
) -> float | None:
    """
    Calculate glucose coefficient of variation (CV).

    Formula:
        CV = SD / Mean × 100
    """

    values = glucose_values(readings)

    if len(values) < 2:
        return None

    avg = mean(values)

    if avg == 0:
        return None

    sd = stdev(values)

    return round((sd / avg) * 100, 1)


# ==========================================================
# Variability Classification
# ==========================================================

def variability_level(
    readings: list[dict],
) -> str:
    """
    Classify glucose variability.

    Clinical interpretation:

    < 36%   Stable
    36–50%  Moderate
    > 50%   High
    """

    cv = coefficient_of_variation(readings)

    if cv is None:
        return "Unknown"

    if cv < 36:
        return "Stable"

    if cv <= 50:
        return "Moderate"

    return "High"


# ==========================================================
# Variability Score
# ==========================================================

def variability_score(
    readings: list[dict],
) -> int:
    """
    Return a variability score from 0–100.

    Higher is better.
    """

    cv = coefficient_of_variation(readings)

    if cv is None:
        return 0

    score = max(0, 100 - int(cv))

    return score


# ==========================================================
# Summary
# ==========================================================

def summary(
    readings: list[dict],
) -> dict:
    """
    Return all variability metrics.
    """

    return {
        "standard_deviation": standard_deviation(readings),
        "coefficient_of_variation": coefficient_of_variation(readings),
        "variability_level": variability_level(readings),
        "variability_score": variability_score(readings),
    }
