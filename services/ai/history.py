"""
Traven History Service

Retrieve historical CGM data for longitudinal analysis.

Responsibilities
----------------
✓ Retrieve historical readings
✓ Retrieve date ranges
✓ Retrieve rolling windows
✓ Compare periods

This module does NOT:
---------------------
✗ Calculate metrics
✗ Detect glucose patterns
✗ Generate AI insights
"""

from datetime import datetime
from datetime import timedelta


class HistoryService:

    """
    Access historical CGM readings.
    """

    def __init__(self, datastore):

        self.datastore = datastore



def today(
    self,
    patient_id: str,
) -> list[dict]:
    """
    Retrieve today's readings.
    """

    today = datetime.utcnow().date()

    return self.datastore.readings(

        patient_id=patient_id,

        start=today,

        end=today,

    )



def last_days(

    self,

    patient_id: str,

    days: int = 14,

) -> list[dict]:

    """
    Retrieve the last N days.
    """

    end = datetime.utcnow()

    start = end - timedelta(days=days)

    return self.datastore.readings(

        patient_id=patient_id,

        start=start,

        end=end,

    )


def between(

    self,

    patient_id: str,

    start,

    end,

) -> list[dict]:

    """
    Retrieve a custom date range.
    """

    return self.datastore.readings(

        patient_id=patient_id,

        start=start,

        end=end,

    )



def previous_week(

    self,

    patient_id: str,

) -> list[dict]:

    """
    Retrieve readings from the week before the current one.
    """

    end = datetime.utcnow() - timedelta(days=7)

    start = end - timedelta(days=7)

    return self.datastore.readings(

        patient_id=patient_id,

        start=start,

        end=end,

    )
