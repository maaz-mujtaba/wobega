from sqlalchemy.orm import Session
from fastapi import FastAPI, HTTPException, Depends
from database import get_db
import models
import schemas

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