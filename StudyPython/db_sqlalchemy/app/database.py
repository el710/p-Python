from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import create_engine

##                      //// - absolute path
##                      /// - relative path
DATABASE_URL = "sqlite:///data.db"

# print(f"--------------- Start engine...")
##                                   echo work in termainal
##                                              pool_size = max count of sessions with base
##                                                            10 + 5
engine = create_engine(DATABASE_URL, echo=True, pool_size=10, max_overflow=5)

SessionLocal = sessionmaker(bind=engine) ## !!! watch expire_on_commit parameter...

class Base(DeclarativeBase):
    pass

def get_db():
    with SessionLocal() as session:
        yield session ## give in without close process...