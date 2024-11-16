"""
    ORM Application model Base() for database 'Books'

"""
from ..database import Base
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship, mapped_column, Mapped

"""
    отложенный импорт
    check cycling of import one-another module
"""
# from typing import TYPE_CHECKING
# if TYPE_CHECKING:
#     from .user import User
## + we do it in __init__ file

"""
    Base.metadata.create_all() - makeup related models
    but we use alembic package
"""

class Book(Base):
    __tablename__ = "Books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(length=255))
    author = Column(String(length=50), index=True) ## unique means in email column
    owner_id = Column(Integer, ForeignKey('Users.id'))
    ## new method
    # id: Mapped[int] = mapped_column() 

    ## one book can has one user
    rel_user = relationship("User", back_populates='rel_books')
    ## rel_user: Mapped['User'] = relationship(back_populates='books') # it needs TYPE_CHECKING

