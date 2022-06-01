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
    menu = ["Home", "Spend History", "CreditCard History", "Add Purchase","Bank Members"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Home":
        st.subheader("Home")
        
    elif choice == "Spend History":
        st.subheader("Spend History")
        username= st.text_input("Enter yuor name:")
    elif choice == "CreditCard History":
        form = st.form(key='my_form')
        form.subheader("CreditCard History")
        username= form.text_input("Enter yuor name:")
        submit_button = form.form_submit_button(label='Submit')
    elif choice == "Add Purchase":
        st.subheader("Add Purchase")
        purchasename = st.text_input("Enter purchase name")
        purchasedesc = st.text_area("Enter purchase description")
        totalprice = st.text_input("Enter purchase total price")
        date = st.date_input("Date")
        if st.button("Add"):
            st.success("Post:{} saved".format(purchasename, purchasedesc, totalprice, date))
    
    elif choice == "Bank Members":
        st.subheader("Bank Members")

main()
