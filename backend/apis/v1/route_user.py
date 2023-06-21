from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from schemas.user import UserCreate, ShowUser
from db.session import get_db
from db.repository.user import create_new_user

router = APIRouter()


@router.post("/users",response_model=ShowUser)
def create_user(user : UserCreate,db: Session = Depends(get_db)):
    user = create_new_user(user=user,db=db)
    return user 

