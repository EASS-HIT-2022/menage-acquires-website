
from fastapi.testclient import TestClient
from backend.main import app
import requests
import json

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "welcome to bank project"

def test_add_client():
    response= client.post("/add_account",json={
    "name": "shiran",
    "username": "shiran_dav",
    "password": "Aa123456"
    })
    assert response.status_code == 200
    assert response.json() == "User added to the db succesfully!"


