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

from fastapi import FastAPI

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
@app.get("/user/{first_name}/{last_name}")
async def news(first_name: str, last_name: str) -> dict:
    return {"message": f"Hello, {first_name} {last_name}"}