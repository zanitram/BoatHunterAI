import streamlit as st

from components.ui import render_metric_card
from core.database import get_boats, get_dashboard_stats
from core.models import Boat


def render_analytics_page():
    st.title("📈 Analytics")
    st.caption("Understand your current inventory at a glance.")

    stats = get_dashboard_stats()
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        render_metric_card("Boats tracked", str(stats["total_boats"]), "Total listings")
    with col2:
        render_metric_card("Average score", f"{stats['average_score']:.1f}", "Current quality")
    with col3:
        render_metric_card("Average price", f"${stats['average_price']:,.0f}", "Typical spend")
    with col4:
        render_metric_card("Best score", str(stats["top_score"]), "Top-ranked listing")

    boats = [Boat.from_row(row) for row in get_boats()]
    if not boats:
        st.info("Add boats to see analytics.")
        return

    ranked = sorted(boats, key=lambda item: item.score, reverse=True)
    st.subheader("Top ranked boats")
    for boat in ranked[:5]:
        st.write(f"- {boat.name} — score {boat.score} — ${boat.price:,.0f}")
