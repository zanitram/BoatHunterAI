import streamlit as st


def render_metric_card(title, value, subtitle=""):
    st.markdown(
        f"""
        <div class="metric-card">
            <div style="font-size: 0.9rem; color: #94a3b8;">{title}</div>
            <div style="font-size: 1.6rem; font-weight: 700; color: #f8fafc; margin-top: 0.3rem;">{value}</div>
            <div style="font-size: 0.85rem; color: #64748b; margin-top: 0.2rem;">{subtitle}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_boat_card(boat, on_edit=None, on_delete=None):
    score_color = "#22c55e" if boat.score >= 80 else "#f59e0b" if boat.score >= 60 else "#ef4444"
    st.markdown(
        f"""
        <div class="boat-card">
            <div style="display:flex; justify-content:space-between; align-items:center; gap:1rem; flex-wrap:wrap;">
                <div>
                    <div style="font-size: 1.15rem; font-weight: 700; color: #f8fafc;">{boat.name}</div>
                    <div style="color: #94a3b8; margin-top: 0.2rem;">{boat.location}</div>
                </div>
                <div style="background: {score_color}; color: #020617; padding: 0.35rem 0.7rem; border-radius: 999px; font-weight: 700;">
                    Score {boat.score}
                </div>
            </div>
            <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 0.75rem; margin-top: 0.8rem; color: #cbd5e1;">
                <div><strong>Price</strong><br />${boat.price:,.0f}</div>
                <div><strong>Engine</strong><br />{boat.engine}</div>
                <div><strong>Length</strong><br />{boat.length:.1f} ft</div>
                <div><strong>Trailer</strong><br />{'Yes' if boat.trailer else 'No'}</div>
            </div>
            <div style="margin-top: 0.8rem; color: #94a3b8;">{boat.notes or 'No notes yet.'}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([1, 1])
    if on_edit:
        col1.button("Edit", key=f"edit_{boat.id}", on_click=on_edit, args=(boat,))
    if on_delete:
        col2.button("Delete", key=f"delete_{boat.id}", type="secondary", on_click=on_delete, args=(boat,))
