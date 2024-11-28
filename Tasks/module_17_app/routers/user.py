from fastapi import APIRouter, HTTPException

from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import Depends, status
from sqlalchemy import select, insert, update, delete
from slugify import slugify

from backend.db_depends import get_db
from models.user import UserModel
from schemas import *


user_router = APIRouter(prefix="/user", tags=["User"])

@user_router.get("/")
async def all_users(db: Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(UserModel).where()).all()
    return users
    

@user_router.get("/user_id")
async def user_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalar(select(UserModel).where(UserModel.id == user_id))
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User {user_id} not found")
    return user


@user_router.post("/create")
async def create_user(db: Annotated[Session, Depends(get_db)], user: CreateUser):
    db.execute(insert(UserModel).values(username = user.username,
                                        firstname = user.firstname,
                                        lastname = user.lastname,
                                        age = user.age,
                                        slug = slugify(user.username)))
    db.commit()
    return {"status_code": status.HTTP_200_OK, "transaction": f"User {user.username} created"}


@user_router.put("/update")
async def update_user(db: Annotated[Session, Depends(get_db)], user_id: int, user: UpdateUser):
    item = db.scalar(select(UserModel).where(UserModel.id == user_id))
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User {user_id} not found")
    db.execute(update(UserModel).where(UserModel.id == user_id).values(firstname = user.firstname,
                                                                       lastname = user.lastname,
                                                                       age = user.age))
    db.commit()
    return {"status_code": status.HTTP_200_OK, "transaction": f"User {user_id} updated"}


@user_router.delete("/delete")
async def delete_user(db: Annotated[Session, Depends(get_db)], user_id: int):
    item = db.scalar(select(UserModel).where(UserModel.id == user_id))
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User {user_id} not found")
    
    db.execute(delete(UserModel).where(UserModel.id == user_id))
    db.commit()

    return {"status_code": status.HTTP_200_OK, "transaction": f"User {user_id} deleted"}