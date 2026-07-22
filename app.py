import streamlit as st
from core.database import initialize
from core.config import APP_NAME

# Create database if it doesn't exist
initialize()

st.set_page_config(
    page_title=APP_NAME,
    page_icon="🚤",
    layout="wide"
)

st.sidebar.title("🚤 Boat Hunter")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Add Boat",
        "Saved Boats",
        "Compare",
        "Settings"
    ]
)

st.title(APP_NAME)

if page == "Dashboard":

    st.header("Dashboard")

    c1, c2, c3 = st.columns(3)

    c1.metric("Boats", "0")
    c2.metric("Buy Now", "0")
    c3.metric("Average Score", "0")

    st.info("Database connected successfully!")

elif page == "Add Boat":

    st.header("Add Boat")

    st.write("Coming next...")

elif page == "Saved Boats":

    st.header("Saved Boats")

elif page == "Compare":

    st.header("Compare Boats")

elif page == "Settings":

    st.header("Settings")