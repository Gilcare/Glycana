"""
Traven Card Components.

Reusable UI cards used throughout the application.


It should:

✅ Accept data
✅ Display information
✅ Apply Traven styling

It should NOT:

❌ Calculate glucose metrics
❌ Call AI models
❌ Query databases
"""

import streamlit as st

from core.theme import PRIMARY, ACCENT, SECONDARY



# ==========================================================
# Generic Card
# ==========================================================


def card(
    title: str,
    content: str,
    icon: str = "") -> None:
    """
    Generic Traven card.
    """

    st.markdown(
        f"""
        <div class="card">

            <div class="card-header">

                <span>
                    {icon}
                </span>

                <strong>
                    {title}
                </strong>

            </div>


            <div class="card-content">

                {content}

            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )



# ==========================================================
# Metric Card
# ==========================================================


def metric_card(
    label: str,
    value: str,
    description: str = "",
    icon: str = ""
) -> None:
    """
    Large number display card.

    Examples:
    - Current glucose
    - Time in range
    - Average glucose
    """

    html = f"""
    <div class="metric-card">

    <div class="metric-label">
        {icon} {label}
    </div>

    <div class="metric-value">
        {value}
    </div>

    <div class="metric-description">
        {description}
    </div>

    </div>
    """
    
    st.code(html)
    
    st.markdown(
        html,
        unsafe_allow_html=True,
    )




# ==========================================================
# Insight Card
# ==========================================================

def insight_card(
    title: str,
    message: str,
) -> None:
    """
    AI-generated insight card.
    """

    with st.container(border=True):

        st.markdown(f"### 🧠 {title}")

        st.write(message)


# ==========================================================
# Sensor Card
# ==========================================================


def sensor_card(
    device_name: str,
    status: str,
    connected: bool = False
) -> None:
    """
    Pure native CGM device status card.
    """
    indicator = "🟢" if connected else "🔴"
    
    with st.container(border=True):
        # Create a mini grid layout inside the card container
        left_col, right_col = st.columns([3, 1], vertical_alignment="center")
        
        with left_col:
            st.markdown(f"### {device_name}")
            st.caption(f"Status: {status}")
            
        with right_col:
            # Displays a clean badge/metric representation on the right side
            st.metric(label="State", value=indicator, label_visibility="collapsed")



def sensor_card2(
    device_name: str,
    status: str,
    connected: bool = False
) -> None:
    """
    CGM device status card.
    """

    indicator = "🟢" if connected else "🔴"


    st.markdown(
        f"""
        <div class="sensor-card">

            <strong>
                {device_name}
            </strong>


            <p>

                {indicator} {status}

            </p>

        </div>
        """,
        unsafe_allow_html=True,
    )
