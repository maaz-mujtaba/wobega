from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app import models
from app import schemas
import uuid
from app.database import get_db
from datetime import datetime

def get_seller(email : str, db : Session = Depends(get_db)):
    return db.query(models.businesses).filter(models.businesses.email == email).first()

def create_seller(seller : schemas.BusinessBase, db : Session = Depends(get_db)):
    if get_seller(seller.email):
        raise HTTPException(
            status_code=401,
            detail= "User Already exists"
        )
    new_seller = models.businesses(
        business_id = seller.business_id,
        owner_id = seller.owner_id,
        name = seller.name,
        email = seller.email,
        address = seller.address
    )
    db.add(new_seller)
    db.commit()
    db.refresh(new_seller)
    return new_seller