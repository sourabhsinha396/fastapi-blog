from apis.base import api_router
from apps.base import app_router
from core.config import settings
from db.base import Base
from db.session import engine
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


def create_tables():
    Base.metadata.create_all(bind=engine)


def include_router(app):
    app.include_router(api_router)
    app.include_router(app_router)


def configure_staticfiles(app):
    app.mount("/static", StaticFiles(directory="static"), name="static")


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    create_tables()
    include_router(app)
    configure_staticfiles(app)
    return app


app = start_application()
