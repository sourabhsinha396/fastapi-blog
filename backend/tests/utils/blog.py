from db.repository.blog import create_new_blog
from schemas.blog import CreateBlog
from sqlalchemy.orm import Session
from tests.utils.user import create_random_user


def create_random_blog(db: Session):
    blog = CreateBlog(title="first_blog", content="Tests make the system stable!")
    user = create_random_user(db=db)
    blog = create_new_blog(blog=blog, db=db, author_id=user.id)
    return blog
