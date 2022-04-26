
from fastapi.testclient import TestClient
from main import app
import requests
import json

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "welcome to bank project"

def test_add_client():
    response= client.post("/createuser",json={
    "firstname": "shiran",
    "lastname": "davidov",
    "username": "shiran_dav",
    "password": "Aa123456"
    })
    assert response.status_code == 200
    assert response.json() == {f"message": "The client shiran davidov created successfuly!"}


