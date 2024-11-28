"""
    Schemas = data structures to input, validated by pydentic
    
    Pydentic allows:
     - validation of input data
     - auto making documentation in Swagger

"""

from pydantic import BaseModel

class Category(BaseModel):
    id: int
    name: str
    class Config():
        orm_mode = True   ## object can create from ORM(SQLAlchemy)
    parent_id: int | None
    
class CreateCategory(BaseModel): ## for create ('id' will auto generate)
    name: str
    parent_id: int | None


class Product(BaseModel):
    id: int
    name: str
    category_id: int
    class Config():
        orm_model = True
    description: str
    price: int
    image_url: str
    stock: int        
    
class CreateProduct(BaseModel):
    name: str
    description: str
    price: int
    image_url: str
    stock: int
    category_id: int

