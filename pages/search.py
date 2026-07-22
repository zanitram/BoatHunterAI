import streamlit as st

from components.ui import render_boat_card
from core.database import add_boat, delete_boat, get_boats, update_boat
from core.models import Boat
from core.scoring import calculate_score


def render_search_page():
    st.title("🧭 Inventory")
    st.caption("Add, edit, and manage your boat listings with full SQLite CRUD support.")

    if "editing_boat_id" not in st.session_state:
        st.session_state.editing_boat_id = None

    edit_boat = None
    edit_id = st.session_state.editing_boat_id
    if edit_id is not None:
        row = next((row for row in get_boats() if row[0] == edit_id), None)
        if row:
            edit_boat = Boat.from_row(row)

    default_name = edit_boat.name if edit_boat else ""
    default_price = edit_boat.price if edit_boat else 10000
    default_location = edit_boat.location if edit_boat else ""
    default_engine = edit_boat.engine if edit_boat else ""
    default_length = edit_boat.length if edit_boat else 24.0
    default_trailer = edit_boat.trailer if edit_boat else True
    default_notes = edit_boat.notes if edit_boat else ""

    boat_form = st.form("boat_form", clear_on_submit=True)
    with boat_form:
        st.subheader("Boat details")
        name = st.text_input("Boat name", value=default_name)
        price = st.number_input("Price", min_value=0, step=100, value=default_price)
        location = st.text_input("Location", value=default_location)
        engine = st.text_input("Engine", value=default_engine)
        length = st.number_input("Length (ft)", min_value=10.0, max_value=80.0, step=1.0, value=default_length)
        trailer = st.checkbox("Trailer included", value=default_trailer)
        notes = st.text_area("Notes", value=default_notes)
        submitted = st.form_submit_button("Save boat")

    if submitted:
        boat = Boat(
            name=name,
            price=int(price),
            location=location,
            engine=engine,
            length=float(length),
            trailer=bool(trailer),
            notes=notes,
        )
        boat.score = calculate_score(boat)
        if edit_id is None:
            add_boat(boat)
            st.success("Boat added successfully.")
        else:
            update_boat(
                edit_id,
                name=boat.name,
                price=boat.price,
                location=boat.location,
                engine=boat.engine,
                length=boat.length,
                trailer=int(boat.trailer),
                score=boat.score,
                notes=boat.notes,
            )
            st.session_state.editing_boat_id = None
            st.success("Boat updated successfully.")
        st.rerun()

    if edit_boat is not None:
        st.info(f"Editing {edit_boat.name}")
        if st.button("Cancel edit"):
            st.session_state.editing_boat_id = None
            st.rerun()

    st.subheader("Saved boats")
    boats = [Boat.from_row(row) for row in get_boats()]
    if not boats:
        st.info("No boats have been added yet.")
        return

    for boat in boats:
        render_boat_card(
            boat,
            on_edit=lambda selected_boat, boat=boat: (
                setattr(st.session_state, "editing_boat_id", selected_boat.id),
                st.rerun(),
            ),
            on_delete=lambda selected_boat, boat=boat: (
                delete_boat(selected_boat.id),
                st.rerun(),
            ),
        )
