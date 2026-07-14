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


def render_timeline(events: list) -> None:
    """
    Render a chronological health timeline.

    Parameters
    ----------
    events:
        List of dictionaries containing:

        {
            "time": "08:30",
            "title": "Breakfast",
            "description": "Glucose increased after meal",
            "status": "normal"
        }

    """

    if not events:
        st.info("No events available yet.")
        return


    st.markdown(
        """
        <div class="timeline">
        """,
        unsafe_allow_html=True,
    )


    for event in events:

        status = event.get(
            "status",
            "normal"
        )


        if status == "warning":
            icon = "🟠"

        elif status == "critical":
            icon = "🔴"

        else:
            icon = "🟢"


        st.markdown(
            f"""
            <div class="timeline-item">

                <div class="timeline-dot">

                    {icon}

                </div>


                <div class="timeline-content">

                    <div class="timeline-time">

                        {event["time"]}

                    </div>


                    <strong>

                        {event["title"]}

                    </strong>


                    <p>

                        {event["description"]}

                    </p>

                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )


    st.markdown(
        "</div>",
        unsafe_allow_html=True,
    )
