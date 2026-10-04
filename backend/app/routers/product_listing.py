from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
from app import schemas
from app.services.product_listing_service import create_product_listing, get_product_listing

app = APIRouter()

@app.post("/product_listings/", response_model=schemas.ProductListingBase)
def create_product_listing_endpoint(product_listing: schemas.ProductListingCreate, db: Session = Depends(get_db)):
    return create_product_listing(product_listing=product_listing, db=db)

@app.get("/product_listings/{id}", response_model=schemas.ProductListingBase)
def get_product_listing_endpoint(id: int, db: Session = Depends(get_db)):
    return get_product_listing(id=id, db=db)
