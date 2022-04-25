from email import message 
from pydantic import BaseModel, EmailStr 

class UserInfo(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr
    username: str
    password: str


