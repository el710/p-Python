"""
    package of models
"""

from .user import User as UserModel
from .book import Book as BookModel
try:
    from ..database import Base
except:
    from database import Base