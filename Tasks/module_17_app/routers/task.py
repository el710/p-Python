from fastapi import (APIRouter,
                     HTTPException,
                     Depends,
                     status
                     )
from typing import Annotated
from sqlalchemy import (select,
                        insert,
                        update,
                        delete
                        )
from sqlalchemy.orm import Session
from slugify import slugify

from models import *

from backend.db_depends import get_db
from schemas import CreateTask, UpdateTask

task_router = APIRouter(prefix="/task", tags=["Task"])

@task_router.get("/")
async def all_task(db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(TaskModel).where()).all()
    return tasks

@task_router.get("/task_id")
async def task_by_id(db: Annotated[Session, Depends(get_db)], task_id: int):
    task = db.scalar(select(TaskModel).where(TaskModel.id == task_id))
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task {task_id} not found")
    return task

@task_router.post("/create")
async def create_task(db: Annotated[Session, Depends(get_db)], task: CreateTask):
    user = db.scalar(select(UserModel).where(UserModel.id == task.user_id))
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User {user_id} not found")
    
    db.execute(insert(TaskModel).values(title = task.title,
                                        content = task.content,
                                        priority = task.priority,
                                        completed = False,
                                        user_id = task.user_id,
                                        slug = slugify(task.title)
    ))
    db.commit()
    return {"status_code": status.HTTP_200_OK, "transaction": f"Task for user {task.user_id} created"}

@task_router.put("/update")
async def update_task(db: Annotated[Session, Depends(get_db)], task_id: int, task: UpdateTask):
    task = db.scalar(select(TaskModel).where(TaskModel.id == task_id))
    if task is None:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task {task_id} not found")

    db.execute(update(TaskModel).values(title = task.title,
                                        content = task.content,
                                        priority = task.priority,
                                        slug = slugify(task.title)
                                    ))
    db.commit()
    return {"status_code": status.HTTP_200_OK, "transaction": f"Task {task_id} updated"}

    
@task_router.delete("/delete")
async def delete_task(db: Annotated[Session, Depends(get_db)], task_id: int):
    task = db.scalar(select(TaskModel).where(TaskModel.id == task_id))
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task {task_id} not found")
    db.execute(delete(TaskModel).where(TaskModel.id == task_id))
    db.commit()
    return {"status_code": status.HTTP_200_OK, "transaction": f"Task {task_id} has deleted"}
    