from fastapi import FastAPI
from sqlalchemy import text
import  uvicorn
from app.database import engine
from app.routers import carts, orders, products, sellers, users

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
    return False

if __name__ == "__main__":
    uvicorn.run("app.main:app", host ="0.0.0.0",reload = True)