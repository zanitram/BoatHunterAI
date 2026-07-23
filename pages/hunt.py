import streamlit as st

from components.ui import render_boat_card
from core.database import get_search_profiles
from services.search_manager import SearchManager

def render_hunt_page():
    st.markdown("<div class='section-shell'>", unsafe_allow_html=True)
    st.title("🔎 Hunt")
    st.caption("Run the provider framework and review a merged list of boat opportunities.")
    st.markdown("</div>", unsafe_allow_html=True)

    if "hunt_results" not in st.session_state:
        st.session_state.hunt_results = []
    if "hunt_status" not in st.session_state:
        st.session_state.hunt_status = []

    profiles = get_search_profiles()

    col1, col2 = st.columns([2, 1])
    with col1:
        if profiles:
            selected_profile_name = st.selectbox(
                "Saved profile",
                options=[profile.name for profile in profiles],
                index=0,
            )
            selected_profile = next(
                (profile for profile in profiles if profile.name == selected_profile_name),
                None,
            )
        else:
            selected_profile = None
            st.info("Create a search profile first to make the hunt dynamic.")

        if st.button("🚤 HUNT", use_container_width=True):
            st.session_state.hunt_status = []
            manager = SearchManager()
            progress_text = st.empty()
            progress_bar = st.progress(0)
            total = len(manager.providers)

            def update_status(provider_name, count):
                st.session_state.hunt_status.append((provider_name, count))

            for index, provider in enumerate(manager.providers, start=1):
                progress_text.text(f"Running {provider.name}...")
                progress_bar.progress(index / total)

            results = manager.hunt(selected_profile, status_callback=update_status)
            st.session_state.hunt_results = results
            progress_text.text("Search complete")
            progress_bar.progress(1.0)

    with col2:
        st.markdown("### Search status")
        if st.session_state.hunt_status:
            for name, count in st.session_state.hunt_status:
                st.write(f"{name} ✓")
        else:
            st.write("Waiting for a hunt...")

    st.divider()

    if st.session_state.hunt_results:
        st.markdown(f"### {len(st.session_state.hunt_results)} boats found")
        for boat in st.session_state.hunt_results:
            render_boat_card(boat)
    else:
        st.info("0 boats found")


def main():
    render_hunt_page()


if __name__ == "__main__":
    main()