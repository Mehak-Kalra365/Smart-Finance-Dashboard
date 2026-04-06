from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from src.core.database import engine, Base
from src.models import models
from src.api.auth import router as auth_router
from src.api.records import router as records_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Finance Management API",
    description="API for tracking income and expenses",
    version="1.0.0"
)

@app.get("/status")
def read_root():
    return {"message": "Server is running perfectly!"}

app.include_router(auth_router)
app.include_router(records_router)

app.mount("/", StaticFiles(directory="static", html=True), name="static")