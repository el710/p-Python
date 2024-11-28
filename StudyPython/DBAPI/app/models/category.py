from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship

from app.backend.db import Base
"""
from sqlalchemy.orm import DeclarativeBase
class Base(DeclarativeBase):
    pass
"""

"""
    Table "categories" in DB
"""

class MCategory(Base):
    __tablename__ = "categories"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True) 
    name = Column(String)
    slug = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)
    ## in case if it is subcategory
    parent_id = Column(Integer, ForeignKey("categories.id"), nullable=True)
    ## link "many-to-one"
    products = relationship(argument="MProduct", back_populates="categories")
    

"""
    To check out sql backend
"""
# from sqlalchemy.schema import CreateTable
# print(CreateTable(Category.__table__))