from db.repository.blog import list_blogs
from db.session import get_db
from fastapi import APIRouter
from fastapi import Depends
from fastapi import Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

templates = Jinja2Templates(directory="templates")
router = APIRouter()


@router.get("/")
def home(request: Request, db: Session = Depends(get_db)):
    blogs = list_blogs(db=db)
    return templates.TemplateResponse(
        "blog/home.html", {"request": request, "blogs": blogs}
    )
