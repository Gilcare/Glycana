"""
Preprocessing of Glucose data from incoming CGM raw data payloads

Utility functions for preparing Continuous Glucose Monitor (CGM)
data before any analytics are performed.

Responsibilities
----------------
✓ Sort glucose readings
✓ Remove duplicate readings
✓ Validate glucose values
✓ Unit conversion (mg/dL ↔ mmol/L)
✓ Retrieve latest reading

This module does NOT:
---------------------
✗ Calculate Time in Range
✗ Calculate glucose variability
✗ Detect trends
✗ Generate AI insights
"""

from datetime import datetime


# ==========================================================
# Constants
# ==========================================================

MIN_GLUCOSE = 20      # mg/dL
MAX_GLUCOSE = 600     # mg/dL

MGDL_PER_MMOL = 18.0182


# ==========================================================
# Validation
# ==========================================================

def is_valid_reading(reading: dict) -> bool:
    """
    Check whether a glucose reading is valid.

    Expected format:
    {
        "timestamp": datetime,
        "glucose": 108
    }
    """

    if "timestamp" not in reading:
        return False

    if "glucose" not in reading:
        return False

    glucose = reading["glucose"]

    return MIN_GLUCOSE <= glucose <= MAX_GLUCOSE


def filter_invalid_readings(readings: list[dict]) -> list[dict]:
    """
    Remove invalid glucose readings.
    """

    return [
        reading
        for reading in readings
        if is_valid_reading(reading)
    ]


# ==========================================================
# Sorting
# ==========================================================

def sort_readings(readings: list[dict]) -> list[dict]:
    """
    Sort glucose readings chronologically.
    """

    return sorted(
        readings,
        key=lambda reading: reading["timestamp"]
    )


# ==========================================================
# Duplicate Removal
# ==========================================================

def remove_duplicates(readings: list[dict]) -> list[dict]:
    """
    Remove duplicate timestamps.

    Keeps the first occurrence.
    """

    unique = {}
    
    for reading in sort_readings(readings):
        timestamp = reading["timestamp"]

        if timestamp not in unique:
            unique[timestamp] = reading

    return list(unique.values())


# ==========================================================
# Latest Reading
# ==========================================================

def latest_reading(readings: list[dict]) -> dict | None:
    """
    Return the newest glucose reading.
    """

    if not readings:
        return None

    return sort_readings(readings)[-1]


# ==========================================================
# Unit Conversion
# ==========================================================

def mgdl_to_mmol(value: float) -> float:
    """
    Convert mg/dL to mmol/L.
    """

    return round(value / MGDL_PER_MMOL, 1)


def mmol_to_mgdl(value: float) -> int:
    """
    Convert mmol/L to mg/dL.
    """

    return round(value * MGDL_PER_MMOL)
