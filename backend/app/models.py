from sqlalchemy import Column, Integer, Numeric, String, Boolean, DateTime, TIMESTAMP, text, ForeignKey, UniqueConstraint, bigserial, BIGINT
from database import Base

class Users(Base):
    __tablename__ = "users"

    user_id = Column(BIGINT, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique = True, nullable=False)
    role = Column(String, nullable=False)
    hash_password = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text('now()'))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text('now()'), onupdate=text('now()'))

class businesses(Base):
    __tablename__ = "businesses"

    business_id = Column(BIGINT, primary_key=True, index=True)
    owner_id = Column(BIGINT, ForeignKey("users.user_id"), nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, unique = True, nullable=False)
    address = Column(String, nullable=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text('now()'))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text('now()'), onupdate=text('now()'))

class products(Base):

    __tablename__ = "products"

    product_id = Column(BIGINT, primary_key = True, index = True)
    product_name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    description = Column(text, nullable = True)
    brand = Column(String, nullable=True)
    created_at = Column(TIMESTAMP, default = text('now()'), nullable=False)
    updated_at = Column(TIMESTAMP, default=text('now()'), onupdate=text('now()'), nullable=False)

class product_listings(Base):

    __tablename__ = "product_listings"

    product_listing_id = Column(BIGINT, primary_key = True, index = True)
    item_id = Column(BIGINT, ForeignKey('products.product_id'), nullable=False)
    seller_id = Column(BIGINT, ForeignKey('businesses.business_id'), nullable=False)
    price = Column(Numeric(12,2), nullable=False)
    stock = Column(Integer, nullable=False, default=0)
    created_at = Column(TIMESTAMP, default=text('now()'), nullable=False)
    updated_at = Column(TIMESTAMP,default=text('now()'), onupdate=text('now()'), nullable=False)

class orders(Base):

    __tablename__ = "orders"

    order_id = Column(BIGINT, primary_key=True, index=True)
    customer_id = Column(BIGINT, ForeignKey('users.user_id'), nullable=False)
    status = Column(String, nullable=False)
    total_amount = Column(Numeric(12,2), nullable=False)
    shipping_address = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, default=text('now()'), nullable=False)
    updated_at = Column(TIMESTAMP, default=text('now()'), onupdate=text('now()'), nullable=False)

class order_items(Base):
    __tablename__ = "order_items"

    order_items_id = Column(BIGINT, primary_key=True, index=True)
    order_id = Column(BIGINT, ForeignKey('orders.order_id'), nullable=False)
    product_listing_id = Column(BIGINT, ForeignKey('product_listings.product_listing_id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Numeric(12,2), nullable=False)
    sub_total = Column(Numeric(12,2), nullable=False)

class carts(Base):

    __tablename__ = "carts"

    cart_id = Column(BIGINT, primary_key=True, index=True)
    user_id = Column(BIGINT, ForeignKey('users.user_id'), nullable=False)
    created_at = Column(TIMESTAMP, default=text('now()'), nullable=False)
    updated_at = Column(TIMESTAMP, default=text('now()'), onupdate=text('now()'), nullable=False)

class cart_items(Base):

    __tablename__ = "cart_items"

    cart_items_id = Column(BIGINT, primary_key = True, index = True)
    cart_id = Column(BIGINT, ForeignKey('carts.cart_id'), nullable=False)
    product_listing_id = Column(BIGINT, ForeignKey('product_listings.product_listing_id'), nullable=False)
    quantity = Column(Numeric(8,0), nullable=False)
    created_at = Column(TIMESTAMP, default=text('now()'), nullable=False)  
    updated_at = Column(TIMESTAMP, default=text('now()'), onupdate=text('now()'), nullable=False)