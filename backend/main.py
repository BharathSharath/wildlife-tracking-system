from fastapi import FastAPI
from .models import Base, engine
from .routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)
