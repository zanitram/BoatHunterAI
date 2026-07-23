import streamlit as st

from components.ui import render_boat_card, render_metric_card
from core.database import get_boats, get_dashboard_stats
from core.models import Boat


def render_dashboard():
    st.markdown("<div class='section-shell'>", unsafe_allow_html=True)
    st.title("🚤 Dashboard")
    st.caption("Monitor your shortlist and keep the best cabin cruisers in focus.")
    st.markdown("</div>", unsafe_allow_html=True)

    stats = get_dashboard_stats()
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        render_metric_card("Inventory", str(stats["total_boats"]), "Boats tracked")
    with col2:
        render_metric_card("Avg score", f"{stats['average_score']:.1f}", "Weighted quality")
    with col3:
        render_metric_card("Avg price", f"${stats['average_price']:,.0f}", "Typical market value")
    with col4:
        render_metric_card("Top score", str(stats["top_score"]), "Best-ranked boat")

    boats = [Boat.from_row(row) for row in get_boats()]
    st.subheader("Latest boats")

    if not boats:
        st.info("No boats in the database yet. Use Inventory to add your first listing.")
        return

    for boat in boats[:6]:
        render_boat_card(boat)


def main():
    render_dashboard()


if __name__ == "__main__":
    main()