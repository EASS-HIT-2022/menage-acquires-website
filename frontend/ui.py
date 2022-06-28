import streamlit as st 
import requests
import json
import yfinance as yf



# FastAPI endpoints for add and delete stocks
st.set_page_config(page_title="Menage Acquires Website", page_icon=":moneybag:", layout="wide")

st.sidebar.image('cash.png',channels='BGR',use_column_width='auto',output_format='jpg')


add_aquire_URL = 'http://backend:8000/add_acquires'
ReportInfo_URL = 'http://backend:8000/report_info'
creatuser_URL= 'http://backend:8000/add_account'

menu = ["Home","Add Acquire",  "Create User"]

choice = st.sidebar.selectbox("Menu", menu)

if choice == "Create User":
    st.title("Menage Acquires")
    st.subheader("Create User")
    form= st.form("Create",clear_on_submit=True)

    name = form.text_input("Enter your full name:")
    username= form.text_input("Enter the username you want:")

    if form.form_submit_button('Create'):
        user_dic={
            "name": name,
            "username": username,
        }
        response = requests.post(creatuser_URL, json = user_dic)
        if response.status_code== 200:
            st.success("Success to create the user!")
elif choice == "Home" : 
    st.title("Menage Acquires")
    st.subheader("Add your acquires to our system! ")
    form= st.form("Report",clear_on_submit=True)
# elif choice == "Get Acquire Report":
#     st.title("Menage Acquires")
#     st.subheader("Get Acquire Report")
#     form= st.form("Report",clear_on_submit=True)

#     month = form.text_input("enter the month:")
#     username = form.text_input("enter your username:")

#     if form.form_submit_button('Get Report'):
#         user_dic={
#             "month": month,
#             "username": username,
#         }
#         data = fetch(session,ReportInfo_URL)
#         st.write(data)
        # for item in data:
        #     st.write(f"{item['username']}, {item['category']}, {item['totalprice']}, {item['month']}")
         
elif choice == "Add Acquire":
    st.title("Menage Acquires")
    st.subheader("Add Acquire")
    form= st.form("Add",clear_on_submit=True)

    username= form.text_input("Enter your username:")
    category = form.text_input("Enter the acquire category:")
    totalprice = form.text_input("Enter the total price of the acquire:")
    month = form.text_input("Enter the month on numbers 1-12:")

    if form.form_submit_button('Submit'):
        acquire_dic = {
                        "username": username,
                        "category": category,
                        "totalprice": totalprice,
                        "month": month,
                      }         
        response = requests.post(add_aquire_URL, json = acquire_dic)
        print(response.status_code)
        if response.status_code== 200:
            st.success("Acquire added succesfully!")