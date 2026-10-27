from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.routers.api import app
from app import schemas
from app import models
from app.database import get_db
from datetime import datetime
from app.services.product_service import create_product, get_product, get_all_products

app = APIRouter()

@app.put("/products/")
def add_product(product : schemas.ProductCreate, db : Session = Depends(get_db)):
    new_product = create_product(product,db=db)
    return new_product
    

@app.get("/products/")
def get_products(name : str, db : Session = Depends(get_db)):
    return get_product(name=name, db=db)

@app.get("/products/all/")
def get_all_product(db : Session = Depends(get_db)):
    return get_all_products(db=db)
