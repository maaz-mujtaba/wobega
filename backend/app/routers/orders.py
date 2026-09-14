from api import app
from sqlalchemy.orm import Session
import schemas
import models
from database import get_db
from fastapi import Depends

@app.put("/orders/", response_models = schemas.OrderBase)
def confirm_order(order : schemas.OrderBase, db : Session = Depends(get_db)):
    #pass


@app.get("/orders/")
def get_orders(user_id : int, db : Session = Depends(get_db)):
    pass

@app.get("/orders/{order_id}")
def get_order_status(order_id : int, db : Session = Depends(get_db)):
    pass