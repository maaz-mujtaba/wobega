from sqlalchemy import Column, Integer, String, Boolean, DateTime, TIMESTAMP, text, ForeignKey, UniqueConstraint, bigserial, BIGINT
from database import SessionLocal, Base

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

