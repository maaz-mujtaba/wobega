from fastapi import FastAPI
from sqlalchemy import text
import  uvicorn
from app.database import engine
from app.routers import carts, orders, products, sellers, users, product_listing

app = FastAPI(
    title = "Wobega",
    version = "1.0.0"
)
app.include_router(users.app)
app.include_router(sellers.app)
app.include_router(orders.app)
app.include_router(carts.app)
app.include_router(products.app)
app.include_router(product_listing.app)

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