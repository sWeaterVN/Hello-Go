import streamlit as st  
import datetime
st.set_page_config(page_title="Hello-Go", layout="centered")

# check var
var = 1

if "login" not in st.session_state:
    st.error("You have to login first")
    var = 0
    if st.button("Back"):
        st.switch_page("main.py")
    

if "selected_bike" not in st.session_state:
    st.error("No infomation")
    var = 0
    if st.button("Back"):
        st.switch_page("pages/bike_list.py")

if var:
    st.title("Hello-Go | Bike ifnormation")
    st.divider()   

    bike = st.session_state.selected_bike
    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("Bike information")
        st.image(bike["image"], use_container_width = 1)
        st.write(f"**Name:** {bike['name']}")
        st.write(f"**Price:** {bike['price']}")
        st.write(f"**Status:** {bike['status']}")
    with col2:
        st.subheader("")
        current_time = datetime.datetime.now()
        st.write(f"**Time:** {current_time.strftime('%H:%M')}")
        st.write(f"**frais:** {bike['price']}")
        if st.button("Confirm", type='primary'):
            st.session_state.selected_bike = bike
            st.switch_page("pages/payment.py")

    st.write("")
    if st.button("Back"):
        st.switch_page("pages/bike_list.py")