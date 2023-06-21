from sqlalchemy.orm import Session 
from schemas.blog import CreateBlog
from db.models.blog import Blog


def create_new_blog(blog: CreateBlog, db: Session, author_id:int = 1):
    blog = Blog(**blog.dict(),author_id=author_id)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog


