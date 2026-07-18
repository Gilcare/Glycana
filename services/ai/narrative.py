"""
Traven AI - Narrative Generation

Generate human-readable glucose summaries from structured
analytics and AI outputs.

Responsibilities
----------------
✓ Build narrative context
✓ Build the LLM prompt
✓ Generate a natural-language summary

This module does NOT:
---------------------
✗ Calculate glucose metrics
✗ Detect glucose patterns
✗ Assess risk
✗ Generate recommendations
"""

from datetime import datetime


# ==========================================================
# Context Builder
# ==========================================================

def build_context(
    metrics: dict,
    variability: dict,
    patterns: dict,
    trends: dict,
    risk: dict,
    recommendations: list[dict],
) -> dict:
    """
    Combine all AI outputs into a single context object.
    """

    return {

        "metrics": metrics,

        "variability": variability,

        "patterns": patterns,

        "trends": trends,

        "risk": risk,

        "recommendations": recommendations,

    }


# ==========================================================
# Prompt Builder
# ==========================================================

def build_prompt(
    context: dict,
) -> str:
    """
    Convert structured context into an LLM prompt.
    """

    metrics = context["metrics"]
    variability = context["variability"]
    risk = context["risk"]
    recommendations = context["recommendations"]

    recommendation_text = "\n".join(

        f"- {item['title']}: {item['message']}"

        for item in recommendations

    )

    prompt = f"""
You are Traven AI.

Generate a friendly, medically responsible summary of today's
Continuous Glucose Monitoring (CGM) data.

Requirements

- Maximum 150 words.
- Use simple language.
- Do not diagnose disease.
- Do not recommend medication changes.
- Encourage the user without exaggeration.
- Mention both positive findings and areas needing attention.

Patient Data

Current Glucose:
{metrics["current_glucose"]} mg/dL

Average Glucose:
{metrics["average_glucose"]} mg/dL

Time in Range:
{metrics["time_in_range"]}%

GMI:
{metrics["gmi"]}

Estimated HbA1c:
{metrics["estimated_hba1c"]}

Glucose Variability:
{variability["variability_level"]}

Overall Risk:
{risk["overall"]["level"]}

Reason:
{risk["overall"]["primary_reason"]}

Recommendations

{recommendation_text}

Write the narrative.
"""

    return prompt.strip()


# ==========================================================
# Narrative Generator
# ==========================================================

def generate(
    llm,
    context: dict,
) -> str:
    """
    Generate a narrative using the supplied LLM.

    The LLM object is expected to expose:

        llm.generate(prompt: str) -> str
    """

    prompt = build_prompt(context)

    return llm.generate(prompt)


# ==========================================================
# Summary
# ==========================================================

def summary(
    llm,
    metrics: dict,
    variability: dict,
    patterns: dict,
    trends: dict,
    risk: dict,
    recommendations: list[dict],
) -> dict:
    """
    Generate the final patient narrative.
    """

    context = build_context(

        metrics=metrics,

        variability=variability,

        patterns=patterns,

        trends=trends,

        risk=risk,

        recommendations=recommendations,

    )

    narrative = generate(

        llm=llm,

        context=context,

    )

    return {

        "title": "Today's Story",

        "narrative": narrative,

        "generated_at": datetime.utcnow().isoformat(),

    }
