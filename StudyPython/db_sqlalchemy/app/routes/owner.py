
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

try:
    from database import get_db    
except:
    from ..database import get_db
from crud import create_user, get_user_by_id
from schemas import SchemeUser



router = APIRouter(prefix='/users', tags=['User'])

@router.post('/create')
##                    session: Annotated[Session, Depends(get_db)] 
def create_user_route(user: SchemeUser, session: Session = Depends(get_db)):
    n_user = create_user(user, session)
    return n_user