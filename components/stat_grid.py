"""
Traven Statistics Grid.

Displays compact clinical statistics in a responsive grid.

Responsibilities
----------------
✓ Display key-value statistics
✓ Apply consistent Traven styling
✓ Support multiple column layouts

It should NOT:
--------------
✗ Calculate statistics
✗ Query databases
✗ Call AI models
"""

from __future__ import annotations

import math

import streamlit as st

from core.theme import (
    BORDER,
    CARD_BACKGROUND,
    PRIMARY,
    SECONDARY,
    SHADOW_LIGHT,
)


def render_stat_grid(
    stats: dict[str, str],
    columns: int = 2,
) -> None:
    """
    Render a compact statistics grid.

    Parameters
    ----------
    stats:
        Dictionary mapping statistic labels to values.

        Example:
        {
            "Average": "112 mg/dL",
            "Maximum": "168 mg/dL",
            "Minimum": "82 mg/dL",
            "Time in Range": "84%"
        }

    columns:
        Number of columns to display.
    """

    if not stats:
        st.info("No statistics available.")
        return

    columns = max(1, columns)

    items = list(stats.items())

    rows = math.ceil(len(items) / columns)

    index = 0

    for _ in range(rows):

        cols = st.columns(columns)

        for col in cols:

            if index >= len(items):
                break

            label, value = items[index]

            with col:

                st.markdown(
                    f"""
                    <div style="
                        background:{CARD_BACKGROUND};
                        border:1px solid {BORDER};
                        border-radius:12px;
                        padding:16px;
                        margin-bottom:12px;
                        box-shadow:{SHADOW_LIGHT};
                    ">

                        <div style="
                            color:{SECONDARY};
                            font-size:0.85rem;
                            margin-bottom:6px;
                        ">
                            {label}
                        </div>

                        <div style="
                            color:{PRIMARY};
                            font-size:1.35rem;
                            font-weight:700;
                        ">
                            {value}
                        </div>

                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            index += 1
