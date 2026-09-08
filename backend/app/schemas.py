from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    user_id : int
    name : str
    email : str
    role : str
    phone : Optional[str] = None

class UserCreate(UserBase):
    hash_password : str
    created_at : datetime =  datetime.now()
    updated_at : datetime =  datetime.now()

class BusinessBase(BaseModel):
    business_id : int
    owner_id : int
    name : str
    email : str
    description : Optional[str] = None
    created_at : datetime =  datetime.now()
    updated_at : datetime =  datetime.now()

class ProductBase(BaseModel):
    product_id : int
    product_name : str
    category : str
    description : Optional[str] = None
    brand : Optional[str] = None
    created_at : datetime =  datetime.now()
    updated_at : datetime =  datetime.now()

class ProductListingBase(BaseModel):
    product_listing_id : int
    item_id : int
    seller_id : int
    price : float
    stock : int
    created_at : datetime =  datetime.now()
    updated_at : datetime =  datetime.now()

class OrderBase(BaseModel):
    order_id : int
    customer_id : int
    status : str
    total_amount : float
    shipping_address : str
    created_at : datetime = datetime.now()
    updated_at : datetime = datetime.now()

class OrderItems(BaseModel):
    order_item_id : int
    order_id : int
    product_listing_id : int
    quantity : int
    unit_price : float
    sub_total : float

class OrderItemsCreate(OrderItems):
    pass

class CartBase(BaseModel):
    cart_id : int
    user_id : int
    created_at : datetime = datetime.now()
    updated_at : datetime = datetime.now()

class CartItemBase(BaseModel):
    cart_items_id : int
    cart_id : int
    product_listing_id : int
    quantity : int
    created_at : datetime = datetime.now()
    updated_at : datetime = datetime.now()