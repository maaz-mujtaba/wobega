from fastapi import FastAPI, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
import app.services.cart_service as c
from app.database import get_db
from app.routers.api import app
from app import schemas
from app import models

app = APIRouter()

@app.put("/carts/")
def create(cart : schemas.CartBase, db : Session = Depends(get_db)):
    cart = c.create_cart(cart = cart,db = db)
    return cart

@app.put("/carts/{cart_id}")
def getCartsById(id : int, db : Session = Depends(get_db)):
    cart = c.get_cart(id = id, db = db)
    return cart

@app.put("/carts/{cart_id}/addItem")
def addItem(productId : int, cartId : int, db : Session = Depends(get_db)):
    item = c.add_item_to_cart(productListingId = productId, cartId = cartId, db = db)
    return item

@app.delete("carts/{cart_id}/removeItem")
def removeItem(cart_items_id : int, item_id : int, db : Session = Depends(get_db)):
    flag = c.remove_item_from_kart(cart_items_id=cart_items_id, item_id=item_id, db = db)
    return flag