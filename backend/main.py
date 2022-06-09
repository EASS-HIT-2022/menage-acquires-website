from fastapi import Depends, FastAPI, Body, Request ,HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import uvicorn 
from pydantic import BaseModel
from email import message
from  matplotlib.pyplot import flag 
#from clients import clientInfo
import json
from typing import List 
# from acquire import acquire
import yfinance as yf
import asyncio
from datetime import date 


app = FastAPI()

class acquire(BaseModel):
    clientname: str
    totalprice: str

class clientInfo(BaseModel):
    name: str
    username: str
    password: str

def home():
    return "welcome to bank project"

@app.post("/add_acquires")
async def acquires(newacquire: acquire):
    data= {"clientname" :newacquire.clientname , "aquire" :newacquire.totalprice}
    fileName='aquirehist.json'
    with open(fileName,"r") as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
    file_data.append(data)
    # convert back to json.
    with open("aquirehist.json","w") as file:
        json.dump(file_data, file)
    return ("Data added succesfully!")
     

@app.post("/add_account")
async def addaccount(newUser: clientInfo):
    data={"name":newUser.name,"username":newUser.username}
    filename='clientsdb.json'
    with open(filename,"r") as file:
    # First we load existing data into a dict.
        file_data = json.load(file)
    file_data.append(data)
    # convert back to json.
    with open(filename,"w") as file:
        json.dump(file_data, file)
    return ("User added to the db succesfully!")

app.get("/")









