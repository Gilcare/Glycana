"""
Traven Glucose Reading Model.

Represents a single CGM glucose measurement.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass
class GlucoseReading:
    """
    Single continuous glucose monitoring reading.
    """

    glucose: float

    timestamp: datetime

    unit: str = "mg/dL"

    device: str | None = None

    trend: str | None = None


    def to_dict(self) -> dict:
        """
        Convert reading to dictionary format.
        """

        return {

            "glucose": self.glucose,

            "timestamp": self.timestamp.isoformat(),

            "unit": self.unit,

            "device": self.device,

            "trend": self.trend,

        }


    @classmethod
    def from_dict(
        cls,
        data: dict,
    ) -> GlucoseReading:
        """
        Create reading from dictionary.
        """

        return cls(

            glucose=data["glucose"],

            timestamp=datetime.fromisoformat(
                data["timestamp"]
            ),

            unit=data.get(
                "unit",
                "mg/dL"
            ),

            device=data.get(
                "device"
            ),

            trend=data.get(
                "trend"
            ),

        )
