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

    bike = st.session_state.selected_bike
    st.title("Hello-Go | Payment")
    st.divider()



    with st.container():
        col1, col2 = st.columns([1, 1])
        with col1:
            st.image(bike['image'], use_container_width = 1)
        
        with col2:
            current_time = datetime.datetime.now()
            st.markdown(f"**Time:** {current_time.strftime('%H:%M')}")
            st.write("")
            st.markdown(f"### Frais: {bike['price']}")
            st.write("")
            if st.button("Confirm", type = 'primary', use_container_width = 1):
                st.success("succesful")
                st.success(f"you have hired {bike['name']}")
                st.balloons()
            
            if "rented_bike" not in st.session_state:
                st.session_state.rented_bike = []

            rental_info = {
                "bike": bike,
                "start_time": current_time,
                "user": st.session_state.username,
                "paid": 1
            }
            st.session_state.rented_bike.append(rental_info)

    st.write("")
    st.info("Thank you for using our service.")
    if st.button("Back"):
        st.switch_page("pages/bike_list.py")
