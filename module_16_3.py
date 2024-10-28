from fastapi import FastAPI, Path
from typing import Annotated


app = FastAPI()


users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
async def call_dictionary() -> dict:
    return users


@app.post("/user/{username}/{age}")
async def registration(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")], age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="24")]) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def change_registration(user_id: str, username: str, age: int) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} has been updated"


@app.delete("/user/{user_id}")
async def delete_registration(user_id: str) -> str:
    users.pop(user_id)
    return f"User {user_id} has been deleted"