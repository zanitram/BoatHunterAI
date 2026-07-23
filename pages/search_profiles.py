import streamlit as st

from core.database import (
    add_search_profile,
    delete_search_profile,
    get_search_profile,
    get_search_profiles,
    update_search_profile,
)
from core.models import SearchCriteria


def render_search_profiles_page():
    st.markdown("<div class='section-shell'>", unsafe_allow_html=True)
    st.title("📝 Search Profiles")
    st.caption("Create reusable search preferences that drive the hunt flow.")
    st.markdown("</div>", unsafe_allow_html=True)

    if "editing_profile_id" not in st.session_state:
        st.session_state.editing_profile_id = None

    edit_profile = None
    edit_id = st.session_state.editing_profile_id
    if edit_id is not None:
        edit_profile = get_search_profile(edit_id)

    default_name = edit_profile.name if edit_profile else "Weekend cruiser"
    default_budget_min = edit_profile.budget_min if edit_profile else 0
    default_budget_max = edit_profile.budget_max if edit_profile else 20000
    default_max_distance = edit_profile.max_distance_km if edit_profile else 250
    default_length_min = edit_profile.length_min if edit_profile else 20.0
    default_length_max = edit_profile.length_max if edit_profile else 30.0
    default_brands = edit_profile.brands if edit_profile else ""
    default_engine_preferences = edit_profile.engine_preferences if edit_profile else ""
    default_freshwater_only = edit_profile.freshwater_only if edit_profile else False
    default_trailer_required = edit_profile.trailer_required if edit_profile else False

    with st.form("profile_form", clear_on_submit=True):
        st.subheader("Profile details")
        name = st.text_input("Profile name", value=default_name)
        budget_min = st.number_input("Budget min", min_value=0, step=1000, value=default_budget_min)
        budget_max = st.number_input("Budget max", min_value=0, step=1000, value=default_budget_max)
        max_distance_km = st.number_input("Maximum distance (km)", min_value=0, step=50, value=default_max_distance)
        length_min = st.number_input("Length min (ft)", min_value=10.0, max_value=80.0, step=1.0, value=default_length_min)
        length_max = st.number_input("Length max (ft)", min_value=10.0, max_value=80.0, step=1.0, value=default_length_max)
        brands = st.text_input("Brands", value=default_brands)
        engine_preferences = st.text_input("Engine preferences", value=default_engine_preferences)
        freshwater_only = st.checkbox("Freshwater only", value=default_freshwater_only)
        trailer_required = st.checkbox("Trailer required", value=default_trailer_required)
        submitted = st.form_submit_button("Save profile")

    if submitted:
        profile = SearchCriteria(
            name=name,
            budget_min=int(budget_min),
            budget_max=int(budget_max),
            max_distance_km=int(max_distance_km),
            length_min=float(length_min),
            length_max=float(length_max),
            brands=brands,
            engine_preferences=engine_preferences,
            freshwater_only=bool(freshwater_only),
            trailer_required=bool(trailer_required),
        )
        if edit_id is None:
            add_search_profile(profile)
            st.success("Search profile created.")
        else:
            update_search_profile(
                edit_id,
                name=profile.name,
                budget_min=profile.budget_min,
                budget_max=profile.budget_max,
                max_distance_km=profile.max_distance_km,
                length_min=profile.length_min,
                length_max=profile.length_max,
                brands=profile.brands,
                engine_preferences=profile.engine_preferences,
                freshwater_only=int(profile.freshwater_only),
                trailer_required=int(profile.trailer_required),
            )
            st.session_state.editing_profile_id = None
            st.success("Search profile updated.")
        st.rerun()

    if edit_profile is not None:
        st.info(f"Editing {edit_profile.name}")
        if st.button("Cancel edit"):
            st.session_state.editing_profile_id = None
            st.rerun()

    st.subheader("Saved profiles")
    profiles = get_search_profiles()
    if not profiles:
        st.info("No search profiles yet.")
        return

    for profile in profiles:
        st.markdown("---")
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"### {profile.name}")
            st.caption(
                f"Budget ${profile.budget_min} - ${profile.budget_max or 'any'} | "
                f"Max distance {profile.max_distance_km or 'any'} km | "
                f"{profile.length_min or '?'} - {profile.length_max or '?'} ft"
            )
            if profile.brands:
                st.write(f"Brands: {profile.brands}")
            if profile.engine_preferences:
                st.write(f"Engine: {profile.engine_preferences}")
            st.write(f"Freshwater only: {'Yes' if profile.freshwater_only else 'No'}")
            st.write(f"Trailer required: {'Yes' if profile.trailer_required else 'No'}")
        with col2:
            if st.button("Edit", key=f"edit-{profile.id}"):
                st.session_state.editing_profile_id = profile.id
                st.rerun()
            if st.button("Delete", key=f"delete-{profile.id}"):
                delete_search_profile(profile.id)
                st.rerun()


def main():
    render_search_profiles_page()


if __name__ == "__main__":
    main()
