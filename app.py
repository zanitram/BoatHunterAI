import streamlit as st

from core.database import initialize, add_boat, get_boats
from core.models import Boat
from core.scoring import calculate_score
from core.config import APP_NAME

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
        "Add Boat"
    ]
)

# ---------------- Dashboard ----------------

if page == "Dashboard":

    st.title(APP_NAME)

    boats = get_boats()

    st.metric("Saved Boats", len(boats))

    st.divider()

    if len(boats)==0:

        st.info("No boats saved.")

    else:

        for boat in boats:

            with st.container(border=True):

                st.subheader(boat[1])

                c1,c2,c3=st.columns(3)

                c1.metric("Price",f"${boat[2]:,}")

                c2.metric("Score",boat[7])

                c3.write(boat[3])

                st.write(f"Engine: {boat[4]}")
                st.write(f"Length: {boat[5]}'")

# ---------------- Add Boat ----------------

if page=="Add Boat":

    st.title("Add Boat")

    name=st.text_input("Boat")

    price=st.number_input("Price",step=500)

    location=st.text_input("Location")

    engine=st.text_input("Engine")

    length=st.slider("Length",20.0,35.0,24.0)

    trailer=st.checkbox("Trailer Included",True)

    notes=st.text_area("Notes")

    if st.button("Save Boat"):

        boat=Boat(
            name=name,
            price=price,
            location=location,
            engine=engine,
            length=length,
            trailer=trailer,
            notes=notes
        )

        boat.score=calculate_score(boat)

        add_boat(boat)

        st.success("Boat Saved!")

        st.rerun()