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