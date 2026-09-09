import uuid
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models
import schemas
from app.routers.api import app
from datetime import datetime


@app.post("/sellers/")
def create_seller(seller : schemas.BusinessBase, db : Session = Depends(get_db)):
    existing_seller = db.query(models.businesses).filter(models.businesses.business_id == seller.business_id).first()

    if existing_seller:
        raise HTTPException(
            status_code = 401,
            detail = "Seller Already exist"
        )
    
    new_seller = models.businesses(
        business_id = seller.business_id,
        owner_id = seller.owner_id,
        name = seller.name,
        email = seller.email,
        address = seller.address,
        created_at = datetime.now(),
        updated_at = datetime.now()
    )

    db.add(new_seller)
    db.commit()
    db.refresh()
    return new_seller

@app.get("/sellers/", response_model = List[schemas.BusinessBase])
def get_sellers(db : Session = Depends(get_db)):
    return db.query(models.businesses).all()

@app.get("/sellers/{seller_id}", response_model = List[schemas.BusinessBase])
def get_seller_by_id(id : int, db : Session = Depends(get_db)):

    #check if user exists
    seller = db.query(models.businesses).filter(models.businesses.business_id == id).first()

    if not seller:
        raise HTTPException(
            status_code = 404, 
            detail = "Seller does not exist"
        )
    
    return seller