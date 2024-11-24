"""
    WebAPI + DataBase(sqlalchemy)

    import module_17...
"""


from fastapi import FastAPI
from routers import category

import sys
import os

app = FastAPI()

@app.get("/")
async def welcome():
    return {"message": "My shop"}

app.include_router(category.router)


if __name__ == "__main__":
    dir_name, file_name = os.path.split(sys.argv[0])
    name = os.path.splitext(file_name)[0]
 
    os.chdir(dir_name)
    os.system(f"python -m uvicorn {name}:app")