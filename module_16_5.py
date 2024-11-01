from fastapi import FastAPI, Body, HTTPException, Request
from pydantic import BaseModel
from typing import List
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

templates = Jinja2Templates(directory="templates")
users = []


class Users(BaseModel):
    id: int
    username: str
    age: int


@app.get("/user/{user_id}")
async def call_dictionary(request: Request, user_id: int) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users[user_id]})


@app.get("/")
async def get_all(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "user": users})


@app.post("/user/{username}/{age}")
async def registration(username: str, age: int) -> Users:
    if len(users) == 0:
        user_id = 1
    else:
        user_id = len(users)+1
    k = Users(id=user_id, username=username, age=age)
    users.append(k)
    return k


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
    for user in users:
        if user.id == user_id:
            users.pop(user_id-1)
            return user
    raise HTTPException(status_code=404, detail="User was not found")