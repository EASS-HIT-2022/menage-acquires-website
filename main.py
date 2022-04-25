from fastapi import Depends, FastAPI, Body, Request ,HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import uvicorn 
from email import message
from  matplotlib.pyplot import flag 
from user import UserInfo
import time 
import json
from  typing import List 



app = FastAPI()
oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")
listOfUsers= []

@app.get("/")
def home():
    return "welcome to bank project"

@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    print(form_data)
    with open("userbd.json","r") as json_file:
        json_data = json.load(json_file)
    if json_data:
        password= json_data.get(form_data.username)
        if not password:
            print ("wrong password! please try again")
            raise HTTPException(status_code=403, detail="Incorrect username or password")
    return {"access_token": form_data.username, "token_type": "bearer"}

@app.get("/spend/history")
def spend_history(token: str = Depends(oauth_scheme)):
    print(token)
    with open("spendhist.json","r") as spend_history:
        spend_hist_data = json.load(spend_history)
        if not spend_hist_data.get(token):
            raise HTTPException(status_code=400, detail="Username not found in the spend history DB")
    return{
        "username" :token,
        "spend_hist":spend_hist_data[token]
    }
    
@app.get("/creditcard/history")
def credit_history(token:str = Depends(oauth_scheme)):
    print(token)
    with open("credithist.json","r") as cred_history:
        cred_history_data = json.load(cred_history)
        if not cred_history_data.get(token):
            raise HTTPException(status_code=400, detail="Username not found in the spend history DB")
    return{
        "username" :token,
        "spend_hist":cred_history_data[token]
    }

@app.post("/createuser")
async def createuser(bUser: UserInfo):
    flag = False
    for user in listOfUsers:
        if user.username == bUser.username:
            message =  {"message": "The username " +  user.username+ " is already exist!"}
            flag = True
    if flag == False:
        listOfUsers.append(bUser)
        message = {f"message": "The user " + bUser.firstname + " " + bUser.lastname + " created successfuly!"}
    return message



