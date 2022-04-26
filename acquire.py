from pydantic import BaseModel
from datetime import date 

class acquire(BaseModel):
    clientname: str
    totalprice: int
    date: date

def __init__(self,clientname,totalprice,date):
    self.clientname=clientname
    self.totalprice= totalprice
    self.date=date


