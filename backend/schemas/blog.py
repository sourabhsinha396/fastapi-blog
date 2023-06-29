from typing import Optional
from pydantic import BaseModel, validator
from datetime import date



class CreateBlog(BaseModel):
    title: str 
    slug: str
    content: Optional[str] = None 
    
    @validator('slug', pre=True)
    def generate_slug(cls, slug, values):
        title = values.get('title')
        slug = None
        if title:
            slug = title.replace(" ","-").lower()
        return slug
        

class UpdateBlog(CreateBlog):
    pass


class ShowBlog(BaseModel):
    title:str 
    content: Optional[str]
    created_at: date

    class Config():
        orm_mode = True