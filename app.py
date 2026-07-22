import streamlit as st

from core.config import APP_NAME
from core.database import initialize

initialize()

st.set_page_config(
    page_title=APP_NAME,
    page_icon="🚤",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    :root {
        color-scheme: dark;
    }
    .stApp {
        background: linear-gradient(135deg, #07111f 0%, #0f172a 100%);
        color: #f8fafc;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
    }
    .sidebar .sidebar-content {
        background: #020617;
    }
    .boat-card {
        background: rgba(15, 23, 42, 0.95);
        border: 1px solid rgba(148, 163, 184, 0.2);
        border-radius: 16px;
        padding: 1rem;
        box-shadow: 0 12px 30px rgba(2, 6, 23, 0.35);
        margin-bottom: 1rem;
    }
    .metric-card {
        background: rgba(15, 23, 42, 0.95);
        border: 1px solid rgba(148, 163, 184, 0.2);
        border-radius: 16px;
        padding: 1rem;
        height: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.sidebar.image(
    "https://raw.githubusercontent.com/streamlit/brand/main/logos/mark/streamlit-mark-color.png",
    width=80,
)
st.sidebar.title(APP_NAME)
st.sidebar.caption("Used cabin cruiser intelligence")

page = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Inventory", "Analytics", "Settings"],
    index=0,
    label_visibility="visible",
)

if page == "Dashboard":
    from pages.dashboard import render_dashboard

    render_dashboard()
elif page == "Inventory":
    from pages.search import render_search_page

    render_search_page()
elif page == "Analytics":
    from pages.analytics import render_analytics_page

    render_analytics_page()
else:
    from pages.settings import render_settings_page

    render_settings_page()