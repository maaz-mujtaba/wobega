from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.routers.api import app
import schemas
import models
from database import get_db
from datetime import datetime, timestamp
import services.product_service

@app.put("/products/")
def create_product(product : schemas.ProductBase, db : Session = Depends(get_db)):
    new_product = create_product(product)
    return new_product
    

@app.get("/products/")
def get_products(id : int, db : Session = Depends(get_db)):
    return get_products(id=id, db=db)
