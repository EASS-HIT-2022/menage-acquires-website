from urllib import response
from fastapi import Depends, FastAPI, Body, Request  
from pydantic import BaseModel
from  matplotlib.pyplot import flag 
import json
from typing import List 
from datetime import date 

from database import (
    _add_collection_aquire,
    _add_collection_user,
    _get_user_report
)

app = FastAPI()

class acquire(BaseModel):
    username: str
    category: str
    totalprice: str
    month: str

class reportInfo(BaseModel):
    month: str
    username: str

class clientInfo(BaseModel):
    name: str
    username: str

@app.get("/")
def home():
    return "welcome to bank project"

@app.post("/add_acquires")
async def acquires(newacquire: acquire):
    data= {"name":newacquire.username,"category" :newacquire.category , "month": newacquire.month, "aquire" :newacquire.totalprice}
    response= _add_collection_aquire(data)
    print(response)
    return ("Data added succesfully!")

     
@app.post("/add_account")
async def addaccount(newUser: clientInfo):
    data={"name":newUser.name,"username":newUser.username}
    response= _add_collection_user(data)
    return ("User added to the db succesfully!")

@app.get("/report_info")
async def getReportInfo(report: reportInfo):
    data =_get_user_report(report.username,report.month)
    return data