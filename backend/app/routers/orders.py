from fastapi import FastAPI, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from app import schemas
from app import models
from app.database import get_db
from fastapi import Depends
from app.services import order_services as service



app = APIRouter()

@app.put("/orders/")
def create_order(order : schemas.OrderCreate, cost : float, db : Session = Depends(get_db)):
    order = service.create_order(order = order, cost = cost, db = db)
    return order

@app.put("/orders/{order_id}", response_model = schemas.OrderBase)
def confirm_order(order_id : int, db : Session = Depends(get_db)):
    order = service.create_order(order = order, db = db)
    return order


@app.get("/orders/")
def get_orders(user_id : int, db : Session = Depends(get_db)):
    pass

@app.get("/orders/{order_id}")
def get_order_status(order_id : int, db : Session = Depends(get_db)):
    #status = o.
    pass