from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from app import schemas
from app import models
from app.database import get_db
import uuid

def add_item_to_order(orderItem : schemas.OrderItems, product : schemas.ProductListingBase, db : Session = Depends(get_db)):
    #check if stock is present
    if product.stock <= 0:
        return {"message" : "product is out-of-stock"}
    if orderItem.quantity < product.stock :
        return {"message" : "The stock available is less than you need"}
    
    order_item = models.order_items(
        order_item_id = uuid.uuid4(),
        order_id = orderItem.order_id,
        product_listing_id = orderItem.product_listing_id,
        quantity = orderItem.quantity,
        unit_price = orderItem.unit_price,
        sub_total = orderItem.unit_price * orderItem.quantity
    )
    db.add(order_item)
    db.commit()
    db.refresh(order_item)

    #This will update the stock of the product
    item = db.query(models.product_listings).filter(models.product_listings.product_listing_id == product.product_listing_id).first()
    item.stock -= orderItem.quantity
    db.refresh(item)
    return order_item


def create_order(order : schemas.OrderBase, db : Session = Depends(get_db)):
    order = models.orders(
        order_id = uuid.uuid4(),
        customer_id = order.customer_id,
        status = order.status,
        total_amount = order.total_amount,
        shipping_address = order.shipping_address,
    )
    db.add(order)
    db.commit()
    db.refresh(order)
    return order

def update_status(order : schemas.OrderBase, new_status : str, product_list : schemas.ProductListingBase = None, db : Session = Depends(get_db)):
    statusList = ["Order Confirmed", "Order Shipped", "Order Out for Delivery", "Order Completed", "Order Cancelled"]
    order_to_look = db.query(models.orders).filter(models.orders == order.order_id).first()

    if new_status not in statusList:
        return {"message" : "Invalid Input"}
    
    if new_status == order_to_look.status:
        return {"message" : "Input status is the same as previous status"}
    order_to_look.status = new_status

    if new_status == "Order Cancelled":
        item = db.query(models.product_listings).filter(models.product_listings.product_listing_id == product_list.product_listing_id).first()
        ord = db.query(models.order_items).filter(models.order_items.order_id == order_to_look.order_id).first()
        item.stock += ord.quantity
        db.commit()
        db.refresh(item)
    db.commit()
    db.refresh(order_to_look)
    return order_to_look

def cancel_order(order : schemas.OrderBase, db : Session = Depends(get_db)):
    placed_order = db.query(models.orders).filter(models.orders.order_id == order.order_id).first()

    if not placed_order:
        raise HTTPException(
            status_code= 404,
            detail= "Order does not exist"
        )
    
    update_status(order,"Order Cancelled",db)

    db.commit()
    db.refresh(placed_order)
    return True

def get_status(orderId : int, db : Session = Depends(get_db)):
    