"""
Traven Patient Model.

Represents a patient using the Traven platform.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Patient:
    """
    Represents a patient profile.
    """

    patient_id: str

    first_name: str

    last_name: str

    date_of_birth: datetime | None = None

    sex: str | None = None

    email: str | None = None

    phone: str | None = None

    diabetes_type: str | None = None

    cgm_device: str | None = None

    preferred_unit: str = "mg/dL"

    created_at: datetime = field(
        default_factory=datetime.utcnow
    )

    updated_at: datetime = field(
        default_factory=datetime.utcnow
    )

    active: bool = True


    @property
    def full_name(self) -> str:
        """
        Return the patient's full name.
        """

        return f"{self.first_name} {self.last_name}"


    def to_dict(self) -> dict:
        """
        Convert the patient to a dictionary.
        """

        return {

            "patient_id": self.patient_id,

            "first_name": self.first_name,

            "last_name": self.last_name,

            "date_of_birth": (
                self.date_of_birth.isoformat()
                if self.date_of_birth
                else None
            ),

            "sex": self.sex,

            "email": self.email,

            "phone": self.phone,

            "diabetes_type": self.diabetes_type,

            "cgm_device": self.cgm_device,

            "preferred_unit": self.preferred_unit,

            "created_at": self.created_at.isoformat(),

            "updated_at": self.updated_at.isoformat(),

            "active": self.active,

        }


    @classmethod
    def from_dict(
        cls,
        data: dict,
    ) -> "Patient":
        """
        Create a Patient from a dictionary.
        """

        return cls(

            patient_id=data["patient_id"],

            first_name=data["first_name"],

            last_name=data["last_name"],

            date_of_birth=(
                datetime.fromisoformat(data["date_of_birth"])
                if data.get("date_of_birth")
                else None
            ),

            sex=data.get("sex"),

            email=data.get("email"),

            phone=data.get("phone"),

            diabetes_type=data.get("diabetes_type"),

            cgm_device=data.get("cgm_device"),

            preferred_unit=data.get(
                "preferred_unit",
                "mg/dL",
            ),

            created_at=(
                datetime.fromisoformat(data["created_at"])
                if data.get("created_at")
                else datetime.utcnow()
            ),

            updated_at=(
                datetime.fromisoformat(data["updated_at"])
                if data.get("updated_at")
                else datetime.utcnow()
            ),

            active=data.get("active", True),

        )
