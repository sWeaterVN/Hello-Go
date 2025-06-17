import streamlit as st

st.set_page_config(page_title="Hello-Go", layout="centered")
st.title("Welcome to Hello-Go")

files = "information/information.txt"

if "login" not in st.session_state:
    st.session_state.login = False
if "username" not in st.session_state:
    st.session_state.username = ""


col1, col2 = st.columns(2)

username = st.text_input("Username", key="user_input")
password = st.text_input("Password", type="password", key="pass_input")

with col1:
    if st.button("Sign in"):
        try:
            with open(files, "r") as file:
                accounts = file.readlines()
                for account in accounts:
                    if " : " not in account:
                        continue
                    stored_user, stored_pass = account.strip().split(" : ")
                    if username == stored_user and password == stored_pass:
                        st.session_state.login = 1
                        st.session_state.username = username
                        st.success("Login Successful!")
                        st.switch_page("pages/bike_list.py")
                else:
                    st.error("Login Failed! Invalid username or password.")
        except FileNotFoundError:
            st.error("No accounts found. Please sign up first.")

with col2:
    if st.button("Sign up"):
        if username and password:
            with open(files, "r") as file:
                accounts = file.read()
                if (f"{username} :" in accounts):
                    st.error("Username already exists!")
                    st.stop()

            with open("infomation.txt", "a") as file:
                file.write(f"{username} : {password}\n")
            st.success("Account created successfully!")
        else:
            st.error("Please fill in all fields.")
