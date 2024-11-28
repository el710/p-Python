"""
    Router - API methods for some branch(route) of Web-address with prefix
"""

from schemas import Category, CreateCategory
from fastapi import APIRouter, HTTPException

from fastapi import Depends, status
from sqlalchemy.orm import Session
from typing import Annotated

# from app.models import *
from app.models.category import MCategory
from app.backend.db_depends import get_db
from sqlalchemy import insert, select, update

from slugify import slugify


router = APIRouter(prefix="/category",
                   tags=["Categories"]) ## documentation title  - Swagger

db_category = []

##@router.get("/all_categories", response_model=list[Category])  ## == /category/all_categories"
@router.get("/all_categories")  ## == /category/all_categories"
async def get_all_categories(db: Annotated[Session, Depends(get_db)]):
    categories = db.scalar(select(MCategory).where(MCategory.is_active == True)).all() ## get by select
    return categories

## @router.post("/create", response_model=Category)         ## == "/category/create"
@router.post("/create")         ## == "/category/create"
async def create_category(db: Annotated[Session, Depends(get_db)], category: CreateCategory):
    db.execute(insert(MCategory).values(name=category.name,
                                       parent_id=category.parent_id,
                                       slug=slugify(category.name)
                                    ))
    db.commit()
    return {"status_code": status.HTTP_201_CREATED,
            "transaction": 'Successful'}


# @router.put("/update_category", response_model=Category)
# async def update_category(category: Category):
#     for item in db_category:
#         if item["id"] == category.id:
#             item["name"] = category.name
#             return item
#     raise HTTPException(status_code=404, detail=f"Category {category.id} not found")
@router.put("/update_category")
async def update_category(db: Annotated[Session, Depends(get_db)], category_id: int, category: CreateCategory):
    item = db.scalar(select(MCategory).where(MCategory.id == category_id))
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Category {category_id} not found")
    
    db.execute(update(MCategory).where(MCategory.id == category_id).values(
        name=category.name,
        slug=slugify(category.name),
        parent_id=category.parent_id))
    db.commit()
    return {
        "status_code": status.HTTP_200_OK,
        "transaction": 'Category updated successfully'
    }


@router.delete("/delete/")
async def delete_category(db: Annotated[Session, Depends(get_db)], category_id: int):
    item = db.scalar(select(MCategory).where(MCategory.id == category_id))
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Category {category_id} not found")
    
    db.execute(update(MCategory).where(MCategory.id == category_id).values(is_active=False))
    db.commit()
    return {
        "status_code": status.HTTP_200_OK,
        "transaction": 'Category deleted successfully'
    }


