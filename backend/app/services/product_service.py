from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
from app import schemas
import uuid
from datetime import datetime

def create_product(product : schemas.ProductBase, db : Session = Depends(get_db)):
    #check if a product already exists
    existing_product = db.query(models.products).filter(models.products.product_id == product.product_id).first()

    if existing_product:
        raise HTTPException(
            status_code=401,
            detail="Product Already exists"
        )
    
    new_product = models.products(
        product_id = uuid.uuid4(),
        product_name = product.product_name,
        category = product.category,
        description = product.description,
        brand = product.brand
    )

    db.add(new_product)
    db.commit()
    db.refresh()
    return new_product

def get_product(id : int, db : Session = Depends(get_db)):
    #check if the product does not exist
    product = db.query(models.products).filter(models.products.product_id == id).first()
    if not product:
        raise HTTPException(
            status_code=404,
            detail="The product does not exist"
        )
    return product