import streamlit as st

# Cầu hình trang
st.set_page_config(page_title="Hello-Go", layout="wide")
var = 1
# check var
if "login" not in st.session_state:
    st.error("You have to login first")
    var = 0
    if st.button("Back"):
        st.switch_page("main.py")
if var:
        
    bikes = [
        {"id": 1, "name": "Xe điện XL", "price": "50,000 VND/ngày", "status": "Có sẵn", "available": True, "image": "https://thongnhat.com.vn/wp-content/uploads/2024/05/do-480x320.jpg.webp"},
        {"id": 2, "name": "Xe điện XM", "price": "45,000 VND/ngày", "status": "Có sẵn", "available": True, "image": "https://thongnhat.com.vn/wp-content/uploads/2024/05/xe-dap-thong-nhat-rpd-den-480x320.jpg.webp"},
        {"id": 3, "name": "Xe thể thao", "price": "60,000 VND/ngày", "status": "Đã thuê", "available": False, "image": "https://thongnhat.com.vn/wp-content/uploads/2024/05/xe-dap-thong-nhat-spd-xanh-480x320.jpg.webp"},
        {"id": 4, "name": "Xe touring", "price": "55,000 VND/ngày", "status": "Có sẵn", "available": True, "image": "https://thongnhat.com.vn/wp-content/uploads/2022/02/Untitled-4-e1708935315239-480x320.jpg.webp"},
        {"id": 5, "name": "Xe city", "price": "40,000 VND/ngày", "status": "Đã thuê", "available": False, "image": "https://thongnhat.com.vn/wp-content/uploads/2025/06/be-2-480x320.jpg.webp"},
        {"id": 6, "name": "Xe mountain", "price": "65,000 VND/ngày", "status": "Có sẵn", "available": True, "image": "https://thongnhat.com.vn/wp-content/uploads/2025/05/green-480x320.jpg.webp"},
        {"id": 7, "name": "Xe folding", "price": "48,000 VND/ngày", "status": "Có sẵn", "available": True, "image": "https://thongnhat.com.vn/wp-content/uploads/2023/06/gn-2.0-27-ghi-scaled-e1708931480269-480x320.jpg.webp"},
        {"id": 8, "name": "Xe cargo", "price": "70,000 VND/ngày", "status": "Có sẵn", "available": True, "image": "https://thongnhat.com.vn/wp-content/uploads/2023/06/dsc03923-480x320.webp"},
        {"id": 9, "name": "Xe BMX", "price": "35,000 VND/ngày", "status": "Có sẵn", "available": True, "image": "https://thongnhat.com.vn/wp-content/uploads/2021/02/D501626-720x480.jpg.webp"},
        {"id": 10, "name": "Xe hybrid", "price": "58,000 VND/ngày", "status": "Có sẵn", "available": True, "image": "https://thongnhat.com.vn/wp-content/uploads/2017/08/XDTN_GN0624_Do-720x480.jpg.webp"},
        {"id": 11, "name": "Xe road", "price": "52,000 VND/ngày", "status": "Có sẵn", "available": True, "image": "https://thongnhat.com.vn/wp-content/uploads/2017/09/Untitled-7-720x480.png.webp"},
        {"id": 12, "name": "Xe cruiser", "price": "42,000 VND/ngày", "status": "Có sẵn", "available": True, "image": "https://thongnhat.com.vn/wp-content/uploads/2019/05/thiet-ke-chua-co-ten-480x320.png.webp"}
    ]

    st.title("Welcome to Hello-Go")


    col1, col2 = st.columns([3, 1])

    with col2:
        if st.button("Đăng xuất"):
            st.session_state.logged_in = False
            st.session_state.username = ""
            st.switch_page("main.py")

    st.divider()

    cols = st.columns(4)

    for i, bike in enumerate(bikes):
        with cols[i % 4]:

            st.image(bike["image"], use_container_width = 1)


            if bike["available"]:
                st.success(f" ** {bike['name']} ** ")
                st.write(f"Cost: {bike['price']}")
                st.write(f"Status: {bike['status']}")
                if st.button(f"Frais", key=f"rent_{bike['id']}"):

                    st.session_state.selected_bike = bike
                    st.switch_page("pages/detail.py")
            else:
                st.error(f"** {bike['name']}**")
                st.write(f"Cost: {bike['price']}")
                st.write(f"Status: {bike['status']}")
                st.button(f"unavailable", key=f"unavailable_{bike['id']}", disabled=True)

    st.write("")
    if st.button("Back"):
        st.switch_page("pages/bike_list.py")