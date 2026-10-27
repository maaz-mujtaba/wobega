from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
from app import schemas
import uuid
from datetime import datetime

def create_product(product : schemas.ProductCreate, db : Session):
    #check if a product already exists
    existing_product = db.query(models.products).filter(models.products.product_name == product.product_name).first()

    if existing_product:
        raise HTTPException(
            status_code=401,
            detail="Product Already exists"
        )
    
    new_product = models.products(
        product_name = product.product_name,
        category = product.category,
        description = product.description,
        brand = product.brand
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

def get_product(name : str, db : Session):
    #check if the product does not exist
    product = db.query(models.products).filter(models.products.product_name.ilike(f"%{name}%")).first()
    if not product:
        raise HTTPException(
            status_code=404,
            detail="The product does not exist"
        )
    return product

def get_all_products(db : Session):
    products = db.query(models.products).all()
    if not products:
        raise HTTPException(
            status_code=404,
            detail="No products found"
        )
    return products