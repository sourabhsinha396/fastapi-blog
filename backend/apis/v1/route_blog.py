from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from db.session import get_db
from schemas.blog import ShowBlog, CreateBlog
from db.repository.blog import create_new_blog

router = APIRouter()


@router.post("/blogs",response_model=ShowBlog)
async def create_blog(blog: CreateBlog, db: Session= Depends(get_db)):
    blog = create_new_blog(blog=blog,db=db,author_id=1)
    return blog