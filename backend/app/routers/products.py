from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.routers.api import app
from app import schemas
from app import models
from app.database import get_db
from datetime import datetime, timestamp
from services.product_service import create_product, get_product

@app.put("/products/")
def add_product(product : schemas.ProductBase, db : Session = Depends(get_db)):
    new_product = create_product(product)
    return new_product
    

@app.get("/products/")
def get_products(id : int, db : Session = Depends(get_db)):
    return get_product(id=id, db=db)
