'''import uuid
from typing import List
from fastapi import APIRouter, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
from app import schemas
from app.routers.api import app
from datetime import datetime
from app.services.seller_service import create_seller, get_seller

app = APIRouter()

@app.post("/sellers/", response_model = schemas.BusinessBase)
def create_seller(seller : schemas.BusinessCreate, db : Session = Depends(get_db)):
    return create_seller(seller = seller, db=db)


@app.get("/sellers/", response_model = List[schemas.BusinessBase])
def get_sellers(db : Session = Depends(get_db)):
    return db.query(models.businesses).all()

@app.get("/sellers/{email}", response_model = List[schemas.BusinessBase])
def get_seller_by_email(email : str, db : Session = Depends(get_db)):
    seller =  get_seller(email = email, db = db)
    if not seller:
        raise HTTPException(
            status_code=404,
            detail = "Seller not found"
        )
    return seller
    '''

from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
from app import schemas
from app.services.seller_service import create_seller as service_create_seller, get_seller
from app.services.product_listing_service import (get_products_sold_by_seller, 
                                                create_product_listing, 
                                                get_products_sold_by_seller as service_get_listings)

app = APIRouter()

@app.post("/sellers/", response_model=schemas.BusinessBase)
def create_seller(seller: schemas.BusinessCreate, db: Session = Depends(get_db)):
    return service_create_seller(seller=seller, db=db)

@app.get("/sellers/", response_model=List[schemas.BusinessBase])
def get_sellers(db: Session = Depends(get_db)):
    return db.query(models.businesses).all()

@app.get("/sellers/{email}", response_model=schemas.BusinessBase)
def get_seller_by_email(email: str, db: Session = Depends(get_db)):
    seller = get_seller(email=email, db=db)
    if not seller:
        raise HTTPException(
            status_code=404,
            detail="Seller not found"
        )
    return seller

@app.post("/sellers/{seller_id}/listings")
def add_product_listing(seller_id: int, product_listing: schemas.ProductListingCreate, db: Session = Depends(get_db)):
    product_listing.seller_id = seller_id
    return create_product_listing(product_listing=product_listing, db=db)

@app.get("/sellers/{email}/listings", response_model=List[schemas.ProductListingBase])
def get_products_sold_by_seller(email: str, db: Session = Depends(get_db)):
    return service_get_listings(email=email, db=db)