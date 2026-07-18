"""
Traven AI - Recommendations

Generate evidence-based recommendations from CGM analytics.

Responsibilities
----------------
✓ Generate monitoring recommendations
✓ Generate lifestyle recommendations
✓ Generate follow-up recommendations
✓ Prioritize recommendations
✓ Attach supporting evidence

This module does NOT:
---------------------
✗ Call LLMs
✗ Diagnose disease
✗ Prescribe medications
✗ Adjust insulin doses
"""

from services.analytics.metrics import summary as metric_summary
from services.analytics.patterns import summary as pattern_summary
from services.analytics.variability import summary as variability_summary
from services.ai.risk import summary as risk_summary


# ==========================================================
# Recommendation Helper
# ==========================================================

def recommendation(
    priority: str,
    category: str,
    title: str,
    message: str,
    evidence: dict | None = None,
) -> dict:
    """
    Create a standardized recommendation.
    """

    return {

        "priority": priority,

        "category": category,

        "title": title,

        "message": message,

        "evidence": evidence or {},

    }


# ==========================================================
# Monitoring
# ==========================================================

def monitoring_recommendations(
    readings: list[dict],
) -> list[dict]:
    """
    Recommendations related to glucose monitoring.
    """

    recommendations = []

    risk = risk_summary(readings)

    hypo = risk["hypoglycaemia"]
    hyper = risk["hyperglycaemia"]

    if hypo["level"] != "Low":

        recommendations.append(

            recommendation(

                priority="High",

                category="Monitoring",

                title="Monitor for Low Glucose",

                message=(
                    "Low glucose events were detected. "
                    "Continue monitoring your glucose closely "
                    "and discuss recurrent episodes with your "
                    "healthcare provider."
                ),

                evidence=hypo,

            )

        )

    if hyper["level"] != "Low":

        recommendations.append(

            recommendation(

                priority="Medium",

                category="Monitoring",

                title="Monitor High Glucose",

                message=(
                    "Elevated glucose readings were detected. "
                    "Continue monitoring to determine whether "
                    "this pattern persists."
                ),

                evidence=hyper,

            )

        )

    return recommendations


# ==========================================================
# Lifestyle
# ==========================================================

def lifestyle_recommendations(
    readings: list[dict],
) -> list[dict]:
    """
    Lifestyle-focused recommendations.
    """

    recommendations = []

    metrics = metric_summary(readings)

    variability = variability_summary(readings)

    if metrics["time_in_range"] >= 80:

        recommendations.append(

            recommendation(

                priority="Low",

                category="Lifestyle",

                title="Maintain Current Routine",

                message=(
                    "Your glucose remained within the target "
                    "range for most of the day. Maintaining "
                    "your current routine may help support "
                    "continued stability."
                ),

                evidence={
                    "time_in_range":
                    metrics["time_in_range"]
                },

            )

        )

    if variability["variability_level"] != "Stable":

        recommendations.append(

            recommendation(

                priority="Medium",

                category="Lifestyle",

                title="Reduce Glucose Fluctuations",

                message=(
                    "Noticeable glucose variability was "
                    "detected. Consistent meal timing and "
                    "regular physical activity may help "
                    "support more stable glucose levels."
                ),

                evidence=variability,

            )

        )

    return recommendations


# ==========================================================
# Follow-up
# ==========================================================

def follow_up_recommendations(
    readings: list[dict],
) -> list[dict]:
    """
    Recommendations regarding clinical follow-up.
    """

    recommendations = []

    risk = risk_summary(readings)

    overall = risk["overall"]

    if overall["level"] == "High":

        recommendations.append(

            recommendation(

                priority="High",

                category="Follow-up",

                title="Discuss Results with Your Healthcare Provider",

                message=(
                    "Several glucose patterns suggest that "
                    "additional clinical review may be helpful. "
                    "Consider sharing these results with your "
                    "healthcare provider."
                ),

                evidence=overall,

            )

        )

    return recommendations


# ==========================================================
# Education
# ==========================================================

def education_recommendations(
    readings: list[dict],
) -> list[dict]:
    """
    Educational recommendations.
    """

    recommendations = []

    patterns = pattern_summary(readings)

    if len(patterns["rapid_rises"]) > 0:

        recommendations.append(

            recommendation(

                priority="Low",

                category="Education",

                title="Learn About Glucose Spikes",

                message=(
                    "Rapid increases in glucose were detected. "
                    "Learning how meals, physical activity and "
                    "daily routines influence glucose may help "
                    "you better understand these patterns."
                ),

                evidence={
                    "rapid_rises":
                    len(patterns["rapid_rises"])
                },

            )

        )

    return recommendations


# ==========================================================
# Summary
# ==========================================================

def summary(
    readings: list[dict],
) -> list[dict]:
    """
    Return all recommendations sorted by priority.
    """

    recommendations = []

    recommendations.extend(
        monitoring_recommendations(readings)
    )

    recommendations.extend(
        lifestyle_recommendations(readings)
    )

    recommendations.extend(
        follow_up_recommendations(readings)
    )

    recommendations.extend(
        education_recommendations(readings)
    )

    priority_order = {

        "High": 0,

        "Medium": 1,

        "Low": 2,

    }

    recommendations.sort(

        key=lambda item: priority_order[item["priority"]]

    )

    return recommendations
