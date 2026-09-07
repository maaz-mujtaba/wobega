from fastapi import FastAPI
from sqlalchemy import text

from app.database import engine

app = FastAPI(
    title = "Wobega",
    version = "1.0.0"
)


@app.get("/")
def root():
    return {"message" : "Welcome to Wobega API"}

@app.get("/health")
def health_check():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return {"status" : "healthy"}
    except Exception as e:
        return {"status" : "unhealthy",
            "error" : str(e)}