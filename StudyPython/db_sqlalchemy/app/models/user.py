"""
    ORM Application model User() for database 'Users'

"""

from ..database import Base
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship, mapped_column, Mapped

class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=255))
    email = Column(String(length=50), unique=True) ## unique means in email column
    ## new method
    # id: Mapped[int] = mapped_column() 

    ## ManyToMany - needs secondary base
    ## ManyToOne

    ## OneToMany
    ## one user can has many books
    rel_books = relationship("Book", back_populates='rel_user')

    
    