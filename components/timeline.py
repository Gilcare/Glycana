"""
Traven Timeline Component.

Displays health events in chronological order.

Responsibility of timeline.py

It should:

✅ Display events chronologically
✅ Make glucose journeys understandable
✅ Highlight important moments

It should NOT:

❌ Detect events
❌ Analyse glucose data
❌ Generate AI explanations
"""

import streamlit as st


def render_timeline(events):

    for event in events:

        with st.container(border=True):

            left, right = st.columns([1, 5])

            with left:
                st.caption(event["time"])

            with right:
                st.markdown(
                    f"**{event['title']}**"
                )

                st.write(
                    event["description"]
                )
