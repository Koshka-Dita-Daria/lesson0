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
    users.append(Users)
    if len(users) == 1:
        users[len(users)-1].id = 1
    else:
        users[len(users)-1].id = users[len(users)-2].id+1
    users[len(users)-1].username = username
    users[len(users)-1].age = age
    return users[len(users)-1]


@app.put("/user/{user_id}/{username}/{age}")
async def change_registration(user_id: int, username: str, age: int) -> Users:
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")



@app.delete("/user/{user_id}")
async def delete_registration(user_id: int) -> Users:
    try:
        users.pop(user_id)
        return users[user_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")
