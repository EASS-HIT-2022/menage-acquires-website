import streamlit as st 
import requests
import json
import sys
import yfinance as yf
import pandas as pd
import altair as alt

# FastAPI endpoints for add and delete stocks
backend = "http://backend:8080/"
st.set_page_config(page_title="MyBank", page_icon=":moneybag:", layout="wide")

st.title("Bank Website")
st.sidebar.image('bank-logo.jpg',channels='BGR',use_column_width='auto',output_format='jpg')
def main():
    st.title("MY BANK")
    menu = ["Home", "Add Acquire", "Create User"]
    choice = st.sidebar.selectbox("Menu", menu)
    form = st.form(key='my_form')
    if choice == "Home":
        st.subheader("Home")
    elif choice == "Create User":
        form.subheader("Create User")
        clinetname = form.text_input("Enter your full name:")
        username= form.text_input("Enter the username you want:")
        password = form.text_input("Enter password:")
        if form.form_submit_button(label='Create'):
            st.success("Post:{} Success to create the user!".format(clinetname, username))
    elif choice == "Add Acquire":
        form.subheader("Add Acquire")
        username= form.text_input(label="Enter your username:", key="name")
        totalprice=form.text_input("Enter the total price of the acquire:")
        date = form.date_input("Date")
        if form.form_submit_button(label='Add'):
            response = requests.get(f"{backend}getacquire").json()
            acquire =  response['acquire']
            st.success("Post:{} Adding the acquire".format(username, date))
    elif choice == "Bank Members":
        st.subheader("Bank Members")
main()
