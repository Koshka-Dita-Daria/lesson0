from fastapi import FastAPI, Body, HTTPException
from pydantic import BaseModel
from typing import List


app = FastAPI()


users = []

class Users(BaseModel):
    id: int
    username: str
    age: int


@app.get("/users")
async def call_dictionary() -> List[Users]:
    return users


@app.post("/user/{username}/{age}")
async def registration(username: str, age: int) -> Users:
    if len(users[:-1]) == 0:
        Users.id = 1
    else:
        Users.id = len(users[-1])+1
    Users.age = age
    Users.username = username
    users.append(Users)
    try:
        return users[Users.id-1]
    except IndexError:
        raise HTTPException(status_code=404, detail="Message not found")


@app.put("/user/{user_id}/{username}/{age}")
async def change_registration(user_id: int, username: str, age: int) -> Users:
    try:
        Users.id = user_id
        Users.age = age
        Users.username = username
        return users[user_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")



@app.delete("/user/{user_id}")
async def delete_registration(user_id: int) -> Users:
    try:
        users.pop(user_id-1)
        return users[user_id-1]
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")
