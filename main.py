from fastapi import FastAPI

app = FastAPI()

users = []


@app.get("/")
def get_users():
    return users
