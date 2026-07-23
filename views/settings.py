"""
Traven Settings View.

Manage profile, device and application preferences.
"""

from __future__ import annotations

import streamlit as st

from components.navbar import render_navbar
from core.constants import Pages


def render() -> None:
    """
    Render the Settings page.
    """

    render_navbar(
        page=Pages.SETTINGS,
        user_name="Gerald",
    )

    st.write("")

    st.title("⚙ Settings")

    st.caption(
        "Manage your profile, CGM device and notification preferences."
    )

    st.write("")

    # ==========================================================
    # Profile
    # ==========================================================

    st.subheader("👤 Profile")

    col1, col2 = st.columns(2)

    with col1:

        st.text_input(
            "Full Name",
            value="Gerald",
        )

        st.number_input(
            "Age",
            min_value=1,
            max_value=120,
            value=30,
        )

    with col2:

        st.selectbox(
            "Glucose Units",
            [
                "mg/dL",
                "mmol/L",
            ],
        )

        st.selectbox(
            "Language",
            [
                "English",
            ],
        )

    st.divider()

    # ==========================================================
    # CGM Device
    # ==========================================================

    st.subheader("📡 Connected Device")

    col1, col2 = st.columns([2, 1])

    with col1:

        st.text_input(
            "Current Device",
            value="Aidex-X CGM",
            disabled=True,
        )

    with col2:

        st.success("Connected")

    if st.button(
        "Reconnect Device",
        use_container_width=True,
    ):
        st.info(
            "Bluetooth pairing will be available in a future milestone."
        )

    st.divider()

    # ==========================================================
    # Notifications
    # ==========================================================

    st.subheader("🔔 Notifications")

    high_alert = st.checkbox(
        "High Glucose Alerts",
        value=True,
    )

    low_alert = st.checkbox(
        "Low Glucose Alerts",
        value=True,
    )

    summary = st.checkbox(
        "Daily AI Summary",
        value=True,
    )

    medication = st.checkbox(
        "Medication Reminders",
        value=False,
    )

    st.divider()

    # ==========================================================
    # Privacy
    # ==========================================================

    st.subheader("🔒 Privacy")

    st.checkbox(
        "Share anonymous data to improve Traven AI",
        value=False,
    )

    st.checkbox(
        "Require confirmation before exporting reports",
        value=True,
    )

    st.divider()

    # ==========================================================
    # About
    # ==========================================================

    st.subheader("ℹ About")

    st.markdown(
        """
**Application**

- Version: **0.1 MVP**
- Platform: **Traven**
- AI Engine: **Local LLM (Coming Soon)**

**Support**

support@traven.health
"""
    )

    st.write("")

    if st.button(
        "Save Settings",
        type="primary",
        use_container_width=True,
    ):
        st.success("Settings saved successfully.")

