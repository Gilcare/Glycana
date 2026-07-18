"""
Traven AI - Risk Assessment

Evaluate glucose-related risks using CGM analytics.

Responsibilities
----------------
✓ Assess hypoglycaemia risk
✓ Assess hyperglycaemia risk
✓ Assess glucose variability risk
✓ Produce an overall risk assessment
✓ Explain why each risk level was assigned

This module does NOT:
---------------------
✗ Generate recommendations
✗ Call LLMs
✗ Produce patient narratives
"""

from services.analytics.metrics import summary as metric_summary
from services.analytics.variability import summary as variability_summary
from services.analytics.patterns import summary as pattern_summary


# ==========================================================
# Hypoglycaemia Risk
# ==========================================================

def hypoglycaemia_risk(readings: list[dict]) -> dict:
    """
    Assess hypoglycaemia risk.
    """

    patterns = pattern_summary(readings)

    events = len(patterns["hypoglycaemia"])

    if events == 0:

        level = "Low"

        reason = (
            "No hypoglycaemic events were detected."
        )

    elif events <= 2:

        level = "Moderate"

        reason = (
            f"{events} hypoglycaemic event(s) "
            "were detected below 70 mg/dL."
        )

    else:

        level = "High"

        reason = (
            f"{events} hypoglycaemic events "
            "suggest an increased risk of low glucose."
        )

    return {

        "level": level,

        "reason": reason,

        "events": events,

        "evidence": {
            "threshold": "<70 mg/dL"
        },

    }


# ==========================================================
# Hyperglycaemia Risk
# ==========================================================

def hyperglycaemia_risk(readings: list[dict]) -> dict:
    """
    Assess hyperglycaemia risk.
    """

    patterns = pattern_summary(readings)

    events = len(patterns["hyperglycaemia"])

    if events == 0:

        level = "Low"

        reason = (
            "No hyperglycaemic events were detected."
        )

    elif events <= 3:

        level = "Moderate"

        reason = (
            f"{events} hyperglycaemic event(s) "
            "were detected above 180 mg/dL."
        )

    else:

        level = "High"

        reason = (
            f"{events} hyperglycaemic events "
            "suggest persistent high glucose."
        )

    return {

        "level": level,

        "reason": reason,

        "events": events,

        "evidence": {
            "threshold": ">180 mg/dL"
        },

    }


# ==========================================================
# Variability Risk
# ==========================================================

def variability_risk(readings: list[dict]) -> dict:
    """
    Assess glucose variability risk.
    """

    variability = variability_summary(readings)

    level = variability["variability_level"]
    score = variability["variability_score"]
    cv = variability["coefficient_of_variation"]

    if level == "Stable":

        reason = (
            "Glucose variability is within the recommended range."
        )

    elif level == "Moderate":

        reason = (
            "Moderate glucose variability was detected."
        )

    else:

        reason = (
            "High glucose variability suggests unstable glucose control."
        )

    return {

        "level": level,

        "reason": reason,

        "score": score,

        "evidence": {
            "coefficient_of_variation": cv
        },

    }


# ==========================================================
# Overall Risk
# ==========================================================

def overall_risk(readings: list[dict]) -> dict:
    """
    Determine the patient's overall glucose-related risk.
    """

    hypo = hypoglycaemia_risk(readings)
    hyper = hyperglycaemia_risk(readings)
    variability = variability_risk(readings)

    if hypo["level"] == "High":

        level = "High"
        primary_reason = hypo["reason"]

    elif hyper["level"] == "High":

        level = "High"
        primary_reason = hyper["reason"]

    elif variability["level"] == "High":

        level = "High"
        primary_reason = variability["reason"]

    elif (
        hypo["level"] == "Moderate"
        or hyper["level"] == "Moderate"
        or variability["level"] == "Moderate"
    ):

        level = "Moderate"

        if hyper["level"] == "Moderate":
            primary_reason = hyper["reason"]

        elif hypo["level"] == "Moderate":
            primary_reason = hypo["reason"]

        else:
            primary_reason = variability["reason"]

    else:

        level = "Low"

        primary_reason = (
            "No significant glucose-related risks were detected."
        )

    return {

        "level": level,

        "primary_reason": primary_reason,

        "hypoglycaemia": hypo,

        "hyperglycaemia": hyper,

        "variability": variability,

    }


# ==========================================================
# Summary
# ==========================================================

def summary(readings: list[dict]) -> dict:
    """
    Return the complete glucose risk assessment.
    """

    return {

        "hypoglycaemia": hypoglycaemia_risk(readings),

        "hyperglycaemia": hyperglycaemia_risk(readings),

        "variability": variability_risk(readings),

        "overall": overall_risk(readings),

    }


