from fastapi import FastAPI
import requests
from config import URL

app = FastAPI()


@app.get("/")
def home():
    return {"Status": "Up"}


@app.get("/test2/{id}")
def sample_func(id):
    result = requests.get(URL + f'/{id}')
    return result['Value']
