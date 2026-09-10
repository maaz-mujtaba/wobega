import uuid
from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.routers.api import app
import schemas
import models
from database import get_db
from datetime import datetime, timestamp

@app.put("/products/")
def create_product(product : schemas.ProductBase, db : Session = Depends(get_db)):

    existing_product = db.query(models.products).filter(models.products.product_id == product.product_id).first()

    if existing_product:
        raise HTTPException(
            status_code=404,
            detail = "Product already existing"
        )
    
    new_product = models.products(
        product_id = uuid.uuid4(),
        product_name = product.product_name,
        category = product.category,
        description = product.description,
        brand = product.brand,
        created_at = datetime.now(),
        updated_at = datetime.now()
    )

    db.add(new_product)
    db.commit()
    db.refresh()
    return new_product

@app.get("/products/")
def get_products(id : int, db : Session = Depends(get_db)):
    pass