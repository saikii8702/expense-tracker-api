
from fastapi import FastAPI

from app.database import Base, engine
from app import models
from app.routers import auth, expenses


# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI
app = FastAPI(
    title="Expense Tracker API",
    description="Expense management with JWT authentication",
    version="1.0.0",
)

# Register API routers
app.include_router(auth.router)
app.include_router(expenses.router)


@app.get("/")
def home():
    return {
        "message": "Welcome to Expense Tracker API",
        "docs": "/docs",
    }
