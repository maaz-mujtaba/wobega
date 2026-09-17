from sqlalchemy.orm import Session
from fastapi import FastAPI, HTTPException, Depends
from app.database import get_db
from app import models
from app import schemas

def create_cart(cart : schemas.CartBase, db : Session = Depends(get_db)):
    #check if the cart already exists
    existing_cart = db.query(models.carts).filter(models.carts.cart_id == cart.cart_id or models.carts.user_id == cart.user_id).first()

    if existing_cart:
        raise HTTPException(
            status_code=401,
            detail = "Invalid Request"
        )
    new_cart = models.carts(
        cart_id = cart.cart_id,
        user_id = cart.user_id,
    )
    db.add(new_cart)
    db.commit()
    db.refresh(new_cart)
    return new_cart

def get_cart(id : int, db : Session = Depends(get_db)):
    #check if the cart does not exist
    cart = db.query(models.carts.cart_id == id).first()
    if not cart:
        raise HTTPException(
            status_code=404,
            detail = "The cart does not exist"
        )
    return cart

def add_item_to_cart(productListingId : int, cartId : int, db : Session = Depends(get_db)):
    item_in_kart = db.query(models.cart_items).filter(models.cart_items.product_listing_id == productListingId).first()

    if not item_in_kart:
        raise HTTPException(
            status_code=404,
            detail = "Item does not exist"
        )
    #check if cart is existing
    cart_id = item_in_kart.cart_id

    cart_of_item = db.query(models.carts).filter(models.carts.cart_id == cart_id).first()

    if not cart_of_item:
        raise HTTPException(
            status_code=404,
            detail="The cart_id of cart item is not existing"
        ) 

    db.add(item_in_kart)
    db.commit()
    db.refresh(item_in_kart)
    return item_in_kart

def remove_item_from_kart(cart_items_id : int, item_id : int, db : Session = Depends(get_db)):
    #check is cart_items exist

    item_cart = db.query(models.cart_items).filter(models.cart_items.cart_items_id == cart_items_id).first()

    if not item_cart:
        raise HTTPException(
            status_code=404,
            detail="Cart item non existent"
        )
    db.remove(item_cart)
    db.commit()
    db.refresh(item_cart)
    return True