from fastapi import FastAPI
from routers import task, users

app = FastAPI()


@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}


app.include_router(users.router)
app.include_router(task.router)

