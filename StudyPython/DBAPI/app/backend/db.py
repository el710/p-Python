"""
    DataBase environment...
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from sqlalchemy import Column, Integer, String


engine = create_engine("sqlite:///ecommerce.db", echo=True)

SessionLocal = sessionmaker(bind=engine)

"""
    Correlation beetwin Schemas & DataTables
"""
class Base(DeclarativeBase):
    pass

"""
    Maket of Table "user"

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
"""