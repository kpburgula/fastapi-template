from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"Status": "Up"}


@app.get("/test/{id}")
def sample_func(id):
    return {"Value" : f"This is a test and the value entered is {id}"}
