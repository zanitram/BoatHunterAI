import streamlit as st
from core.database import initialize
from core.config import APP_NAME

initialize()
st.set_page_config(page_title=APP_NAME,page_icon="🚤",layout="wide")
st.title(APP_NAME)
st.write("Welcome to Boat Hunter AI v0.1")
st.info("Project scaffold installed successfully.")
