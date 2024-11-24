from fastapi import FastAPI
from routers.task import task_router
from routers.user import user_router

import sys
import os


app = FastAPI()
app.include_router(task_router)
app.include_router(user_router)

@app.get("/")
async def start():
    return {"message": "Welcome to TaskManager"}


if __name__ == "__main__":
    _dir, _file = os.path.split(sys.argv[0])
    os.chdir(_dir)
    name = os.path.splitext(_file)[0]
    os.system(f"python -m uvicorn {name}:app")

