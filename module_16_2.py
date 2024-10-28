from fastapi import FastAPI, Path
from typing import Annotated
app = FastAPI()
@app.get("/")
async def welcome() -> dict:
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def admin() -> dict:
    return {"message": "Вы вошли как администратор"}
@app.get("/user/{user_id}")
async def number_user(user_id: Annotated[int, Path(ge=1, le=100, idescription="Enter User Id", example="1")]) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}
@app.get("/user/{username}/{age}")
async def info_user(username: Annotated[str, Path(min_length=5, max_length=20, idescription="Enter username", example="UrbanUser")], age: Annotated[int, Path(ge=18, le=120, idescription="Enter age", example="24")]) -> dict:
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
