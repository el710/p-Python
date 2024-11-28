from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship

from app.models import *

"""
    Table "products" in DB
"""

class MProduct(Base):
    __tablename__ = "products"
    __table_args__ = {"keep_existing": True}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    slug = Column(String, unique=True, index=True)
    description = Column(String)
    price = Column(Integer)
    img_url = Column(String)
    stock = Column(Integer)
    ## link "one-to-many" by key(commom id) with category
    category_id = Column(Integer, ForeignKey('categories.id'))
    rating = Column(Float)
    is_active = Column(Boolean, default=True)
    ## link "one-to-one" 
    category = relationship(argument='MCategory', back_populates='products')
    