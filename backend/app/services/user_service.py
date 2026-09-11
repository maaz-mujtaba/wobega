from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import models
import schemas
from database import get_db
import uuid
from typing import List
from datetime import datetime

def get_user(email : str, db : Session = Depends(get_db)):
    user = db.query(models.users).filter(models.users.email == email).first()
    return user

def create_user(user : schemas.userBase, db : Session = Depends(get_db)):
    if (get_user(user.email)):
        raise HTTPException(
            status_code=401,
            detail = "User already exists"
        )
    new_user = models.users(
        user_id = uuid.uuid4(),
        name = user.name,
        email = user.email,
        hashed_password = f"hashed_{user.password}",
        is_active = True,
        role = user.role,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def update_password(email : str, db : Session = Depends(get_db)):
    pass

def get_users(db : Session = Depends(get_db)):
    return db.query(models.users).all()

def delete_user(user : str, db : Session = Depends(get_db)):
    if not get_user(user.email):
        raise HTTPException(
            status_code=404,
            detail = "The user does not exist"
        )
    db.delete(user)
    db.refresh()
    return True
