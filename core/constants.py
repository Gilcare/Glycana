"""
Global constants used throughout Traven.
"""

from enum import Enum



class Pages(str, Enum):

    DASHBOARD = "Dashboard"

    GLUCOSE = "Glucose"

    INSIGHTS = "Insights"

    REPORTS = "Reports"

    SETTINGS = "Settings"



class UserRole(str, Enum):

    PATIENT = "Patient"

    DOCTOR = "Doctor"

    ADMIN = "Admin"



class CGMDevice(str, Enum):

    AIDEX_X = "Aidex-X"

    GLUCORX = "GlucoRx"



class GlucoseStatus(str, Enum):

    NORMAL = "Normal"

    LOW = "Low"

    HIGH = "High"

    CRITICAL = "Critical"
