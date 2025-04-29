from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import insert, select

from schemas.user import User
from models import BookModel, UserModel

"""
    make user...
"""
def create_user(session: Session, user: User):
    db_user = User(name=user.name, email=user.email)
    session.add(db_user)
    session.commit()
    return db_user

## or...
def in_create_user(session: Session, user: User):
    quary = insert(UserModel).values(name=user.name, email=user.email)
    session.execute(quary)
    ## all this make user without callback
    return user ## it just for proform


def get_user_by_id(session: Session, user_id: int):
    user = session.scalar(select(UserModel).where(UserModel.id == user_id))
    if not user:
        raise HTTPException(detail="User not found", status_code=status.HTTP_404_NOT_FOUND)
    return user