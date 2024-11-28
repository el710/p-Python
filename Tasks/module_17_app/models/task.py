
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from backend.db import Base


class TaskModel(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True, )
    slug = Column(String, unique=True, index=True)
    link_user = relationship(argument="UserModel", back_populates="link_tasks")

"""
from sqlalchemy.schema import CreateTable
print(CreateTable(Task.__table__))
"""