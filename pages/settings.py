import streamlit as st


def render_settings_page():
    st.title("⚙️ Settings")
    st.caption("Configure how Boat Hunter AI presents your inventory.")

    with st.container():
        st.subheader("Display preferences")
        dark_mode = st.checkbox("Dark dashboard", value=True)
        show_scores = st.checkbox("Show scores on cards", value=True)
        st.text_input("Default search location", value="Toronto")
        if dark_mode and show_scores:
            st.success("Your preferred dashboard layout is active.")


def main():
    render_settings_page()


if __name__ == "__main__":
    main()