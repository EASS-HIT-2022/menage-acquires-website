from email import message 
from pydantic import BaseModel, EmailStr 

class clientInfo(BaseModel):
    firstname: str
    lastname: str
    username: str
    password: str




