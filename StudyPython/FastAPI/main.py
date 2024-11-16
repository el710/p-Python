"""
    Backend part of Web - API

    FastAPI - framework
    ...
        starlet - base of web-service
        pidentic - verification
        swager - documentation
        corse

    start app with fastapi server:  fastapi dev D:\\EL710\\p-Python\\StudyPython\\FastAPI\\main.py
    it automatically refresh API when code is edited

    start app with uvicorn server:  python -m uvicorn main:app !!!NOTE: must be in work directory to see main.py
"""
"""
basic queries:
- Get: get data from server - adress in string = ?var=value
- Post: forms "buing in web shop"
- Put: send data to server - refresh/replace anything
- Delete: ...
- Patch
...

import module_16

"""

from fastapi import FastAPI, Path
from typing import Annotated
import os
import sys

app = FastAPI()

"""
    Get-request from user...
"""
@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello world"}

@app.get("/main")
async def welcome() -> dict:
    return {"message": "Main Page"}

### it's basic...
### python -m uvicorn main:app !!!NOTE: must be in work directory to see main.py

### request with parameters: /id?username=Vasya&age=34
@app.get("/id")                  
async def id_paginator(username: str = "vasya", age: int = 34) -> dict: ## with values by default
    return {"User": username, "Age": age}


### adress-type request: *.org/user/A/B
# @app.get("/user/{first_name}/{last_name}")
# async def news(first_name: str, last_name: str) -> dict:
#     return {"message": f"Hello, {first_name} {last_name}"}

"""
    Validate data
    Path() - set conditions for input data
        parameters with Path() default should stay in the end of variables list
        but Annotated[] solve this mess
        in Path() are used mnemonics: ge - great or equal (>=), le - less or equal (<=) e.t.c
        
    also see Pidentic()


"""
# @app.get("/user/{username}/{id}")
# async def news(username:str = Path(min_length=3, max_length=15, description="Enter your username", example="meuser")
#                , id:int = Path(ge=0, le=100, description="Enter your id", example="56")) -> dict:
#     return {"message": f"{username}:{id}"}

@app.get("/user/{username}/{id}")
async def news(username: Annotated[str, Path(min_length=3, max_length=15, description="Enter your username", example="meuser")]
               , id: Annotated[int, Path(ge=0, le=100, description="Enter your id", example="56")]
               , tail: str) -> dict: ## use Annotated to avoid warnings about tail, because tail must be first in this list
    return {"message": f"{username}:{id}"}


if __name__ == "__main__":
    dir_name, file_name = os.path.split(sys.argv[0])
    name = os.path.splitext(file_name)[0]
 
    os.chdir(dir_name)
    os.system(f"python -m uvicorn {name}:app")