from fastapi import Depends, FastAPI, Body, Request ,HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import uvicorn 
from email import message
from  matplotlib.pyplot import flag 
from clients import clientInfo
import time 
import json
from typing import List 
from acquire import acquire
import requests
import yfinance as yf
import asyncio

app = FastAPI()
oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")
listOfClients= []

@app.get("/")
def home():
    return "welcome to bank project"

@app.post("/acquires")
async def acquires(newacquire: acquire):
    data= {"client name":newacquire.clientname, "aquire":newacquire.totalprice}
    write_json( data ,"aquirehist.json","historyList")
    message = {f"message": "The history of  " + newacquire.clientname + " acquire added"}
    return message

@app.post("/createuser")
async def createuser(newUser: clientInfo):
    flag = False
    for user in listOfClients:
        if user.username == newUser.username:
            message =  {"message": "The client " +  user.username+ " is already exist!"}
            flag = True
    if flag == False:
        listOfClients.append(newUser)
        message = {f"message": "The client " + newUser.firstname + " " + newUser.lastname + " created successfuly!"}
        data={"clientname":newUser.firstname+ " "+newUser.lastname,"username":newUser.username}
        write_json(data,"clientsdb.json","clientsList")
    return message

def write_json(new_data, filename ,nameoflist):
    with open(filename,'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data[nameoflist].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)
        
@app.get("/getacquire") 
def get_user_acquires(acquire):
    data= yf.Ticker(acquire)
    data['Date']= data.index
    acquire_table={
        "Date": data["Date"].astype(str).tolist(),
        "Clinetname": data["Clinetname"].astype(str).tolist(),
        "Acquire": data["Acquire"].astype(str).tolist(),
    }
    return{"Acquire": acquire_table}#acquire_table}
