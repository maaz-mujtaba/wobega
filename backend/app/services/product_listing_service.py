from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from app import models
from app import schemas
from app.database import get_db


def create_product_listing(product_listing : schemas.ProductListingCreate, db : Session):
    #check if a product listing already exists
    existing_product_listing = db.query(models.product_listings).filter(models.product_listings.item_id == product_listing.item_id,
                                                                        models.product_listings.seller_id == product_listing.seller_id
                                                                        ).first()

    if existing_product_listing:
        raise HTTPException(
            status_code=401,
            detail="Product Listing Already exists"
        )
    
    new_product_listing = models.product_listings(
        item_id = product_listing.item_id,
        seller_id = product_listing.seller_id,
        price = product_listing.price,
        stock = product_listing.stock
    )

    db.add(new_product_listing)
    db.commit()
    db.refresh(new_product_listing)
    return new_product_listing

def get_product_listing(id : int, db : Session):
    #check if the product listing does not exist
    product_listing = db.query(models.product_listings).filter(models.product_listings.product_listing_id == id).first()
    if not product_listing:
        raise HTTPException(
            status_code=404,
            detail="The product listing does not exist"
        )
    return product_listing

def get_products_sold_by_seller(email : str, db : Session):
    #check if the seller exists
    seller = db.query(models.businesses).filter(models.businesses.email == email).first()
    if not seller:
        raise HTTPException(
            status_code=404,
            detail="The seller does not exist"
        )
    
    #get all products sold by the seller
    products_sold = db.query(models.product_listings).filter(models.product_listings.seller_id == seller.business_id).all()
    return products_sold


#Product listing will be made by the sellers