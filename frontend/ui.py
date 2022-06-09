import streamlit as st 
import requests
import json
import yfinance as yf


# FastAPI endpoints for add and delete stocks
st.set_page_config(page_title="MyBank", page_icon=":moneybag:", layout="wide")

st.sidebar.image('bank-logo.jpg',channels='BGR',use_column_width='auto',output_format='jpg')


add_aquire_URL = 'http://backend:8000/add_acquires'
creatuser_URL = 'http://backend:8000/add_account'

menu = ["Add Acquire", "Create User"]

choice = st.sidebar.selectbox("Menu", menu)

if choice == "Create User":
    st.title("Bank Website")
    st.subheader("Create User")
    form= st.form("Create",clear_on_submit=True)

    name = form.text_input("Enter your full name:")
    username= form.text_input("Enter the username you want:")
    password = form.text_input("Enter password:")

    if form.form_submit_button('Create'):
        user_dic={
            "name": name,
            "username": username,
            "password": password
        }
        response = requests.post(creatuser_URL, json = user_dic)
        if response.status_code== 200:
            st.success("Success to create the user!")
elif choice == "Add Acquire":
    st.title("Bank Website")
    st.subheader("Add Acquire")
    form= st.form("Add",clear_on_submit=True)

    clientname = form.text_input("Enter your username:")
    totalprice = form.text_input("Enter the total price of the acquire:")

    if form.form_submit_button('Submit'):
        acquire_dic = {
                        "clientname": clientname,
                        "totalprice": totalprice,
                      }         
        response = requests.post(add_aquire_URL, json = acquire_dic)
        print(response.status_code)
        if response.status_code== 200:
            st.success("Acquire added succesfully!")
