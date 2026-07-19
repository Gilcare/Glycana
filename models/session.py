"""
Traven CGM Session Model.

Represents a Continuous Glucose Monitoring (CGM)
sensor session.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Session:
    """
    Represents a CGM sensor session.
    """

    session_id: str

    patient_id: str

    sensor_id: str

    device_name: str

    started_at: datetime

    ended_at: datetime | None = None

    status: str = "Active"

    sensor_lifetime_days: int = 14

    calibration_required: bool = False

    created_at: datetime = field(
        default_factory=datetime.utcnow
    )


    @property
    def is_active(self) -> bool:
        """
        Returns True if the session is currently active.
        """

        return self.status.lower() == "active"


    def to_dict(self) -> dict:
        """
        Convert the session to a dictionary.
        """

        return {

            "session_id": self.session_id,

            "patient_id": self.patient_id,

            "sensor_id": self.sensor_id,

            "device_name": self.device_name,

            "started_at": self.started_at.isoformat(),

            "ended_at": (
                self.ended_at.isoformat()
                if self.ended_at
                else None
            ),

            "status": self.status,

            "sensor_lifetime_days":
                self.sensor_lifetime_days,

            "calibration_required":
                self.calibration_required,

            "created_at":
                self.created_at.isoformat(),

        }


    @classmethod
    def from_dict(
        cls,
        data: dict,
    ) -> "Session":
        """
        Create a Session from a dictionary.
        """

        return cls(

            session_id=data["session_id"],

            patient_id=data["patient_id"],

            sensor_id=data["sensor_id"],

            device_name=data["device_name"],

            started_at=datetime.fromisoformat(
                data["started_at"]
            ),

            ended_at=(
                datetime.fromisoformat(data["ended_at"])
                if data.get("ended_at")
                else None
            ),

            status=data.get(
                "status",
                "Active",
            ),

            sensor_lifetime_days=data.get(
                "sensor_lifetime_days",
                14,
            ),

            calibration_required=data.get(
                "calibration_required",
                False,
            ),

            created_at=(
                datetime.fromisoformat(
                    data["created_at"]
                )
                if data.get("created_at")
                else datetime.utcnow()
            ),

        )
