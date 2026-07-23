"""
Traven Insights View.

Displays AI-generated insights from the user's glucose data.
"""

import streamlit as st

from components.navbar import render_navbar
from components.cards import insight_card

from core.constants import Pages


# ------------------------------------------------------------------
# Temporary imports
# Replace with your actual service functions if names differ.
# ------------------------------------------------------------------

try:
    from services.ai.narrative import generate_narrative
except ImportError:
    generate_narrative = None

try:
    from services.analytics.risk import assess_risk
except ImportError:
    assess_risk = None

try:
    from services.ai.recommendation import generate_recommendations
except ImportError:
    generate_recommendations = None


def render() -> None:
    """
    Render the AI Insights page.
    """

    render_navbar(
        page=Pages.INSIGHTS,
        user_name="Gerald",
    )

    st.write("")

    # ==============================================================
    # Placeholder metrics
    # Replace with analytics output later
    # ==============================================================

    metrics = {
        "average_glucose": 112,
        "time_in_range": 82,
        "gmi": 6.1,
        "cv": 27,
        "overnight_lows": 0,
    }

    # ==============================================================
    # Narrative
    # ==============================================================

    if generate_narrative:

        try:
            story = generate_narrative(metrics)

        except Exception:

            story = (
                "Your glucose remained stable today. "
                "A moderate rise occurred after lunch "
                "before returning to your target range."
            )

    else:

        story = (
            "Your glucose remained stable today. "
            "A moderate rise occurred after lunch "
            "before returning to your target range."
        )

    insight_card(
        title="Today's Story",
        message=story,
    )

    st.write("")

    # ==============================================================
    # Risk Assessment
    # ==============================================================

    st.subheader("🩺 Risk Assessment")

    if assess_risk:

        try:
            risk = assess_risk(metrics)

        except Exception:

            risk = {
                "level": "Low",
                "score": 18,
                "confidence": 92,
                "reasons": [
                    "Excellent Time in Range",
                    "No overnight hypoglycemia",
                    "Low glucose variability",
                ],
            }

    else:

        risk = {
            "level": "Low",
            "score": 18,
            "confidence": 92,
            "reasons": [
                "Excellent Time in Range",
                "No overnight hypoglycemia",
                "Low glucose variability",
            ],
        }

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Risk Level",
            risk["level"],
        )

    with col2:
        st.metric(
            "Risk Score",
            risk["score"],
        )

    with col3:
        st.metric(
            "Confidence",
            f'{risk["confidence"]}%',
        )

    st.write("")

    st.markdown("### Why?")

    for reason in risk["reasons"]:
        st.markdown(f"• {reason}")

    st.write("")

    # ==============================================================
    # Recommendations
    # ==============================================================

    st.subheader("💡 Recommendations")

    if generate_recommendations:

        try:
            recommendations = generate_recommendations(
                metrics,
                risk,
            )

        except Exception:

            recommendations = [
                "Continue your current breakfast routine.",
                "Take a 10-minute walk after lunch.",
                "Stay hydrated throughout the day.",
            ]

    else:

        recommendations = [
            "Continue your current breakfast routine.",
            "Take a 10-minute walk after lunch.",
            "Stay hydrated throughout the day.",
        ]

    for i, recommendation in enumerate(recommendations, start=1):

        st.markdown(
            f"**{i}.** {recommendation}"
        )

    st.write("")

    # ==============================================================
    # Clinical Summary
    # ==============================================================

    st.subheader("📊 Clinical Summary")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Average Glucose",
            "112 mg/dL",
        )

        st.metric(
            "Time in Range",
            "82%",
        )

    with col2:

        st.metric(
            "Estimated GMI",
            "6.1%",
        )

        st.metric(
            "Coefficient of Variation",
            "27%",
        )
