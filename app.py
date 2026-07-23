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
        background:
            radial-gradient(circle at top left, rgba(34, 211, 238, 0.16), transparent 26%),
            linear-gradient(135deg, #020617 0%, #0f172a 45%, #111827 100%);
        color: #f8fafc;
        font-family: "Inter", "Segoe UI", sans-serif;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
    }
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #020617 0%, #0f172a 100%);
        border-right: 1px solid rgba(148, 163, 184, 0.16);
    }
    [data-testid="stSidebarNavItems"] button {
        border-radius: 12px;
        margin: 0.2rem 0;
        padding: 0.6rem 0.8rem;
    }
    [data-testid="stSidebarNavItems"] button[aria-pressed="true"] {
        background: rgba(34, 211, 238, 0.16);
        color: #f8fafc;
    }
    .boat-card {
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.96), rgba(30, 41, 59, 0.96));
        border: 1px solid rgba(148, 163, 184, 0.18);
        border-radius: 20px;
        padding: 1.1rem 1.2rem;
        box-shadow: 0 18px 40px rgba(2, 6, 23, 0.35);
        margin-bottom: 1rem;
        backdrop-filter: blur(10px);
    }
    .metric-card {
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.95), rgba(30, 41, 59, 0.95));
        border: 1px solid rgba(148, 163, 184, 0.18);
        border-radius: 18px;
        padding: 1rem 1rem 1.1rem;
        height: 100%;
        box-shadow: 0 10px 24px rgba(2, 6, 23, 0.25);
    }
    .section-shell {
        background: rgba(15, 23, 42, 0.55);
        border: 1px solid rgba(148, 163, 184, 0.14);
        border-radius: 22px;
        padding: 1.25rem;
        margin-bottom: 1rem;
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
st.sidebar.caption("Premium used cabin cruiser intelligence")

pages = [
    st.Page("pages/dashboard.py", title="Dashboard", icon="🚤"),
    st.Page("pages/search.py", title="Inventory", icon="🧭"),
    st.Page("pages/search_profiles.py", title="Search Profiles", icon="📝"),
    st.Page("pages/hunt.py", title="Hunt", icon="🔎"),
    st.Page("pages/analytics.py", title="Analytics", icon="📈"),
    st.Page("pages/settings.py", title="Settings", icon="⚙️"),
]

page = st.navigation(pages)
page.run()