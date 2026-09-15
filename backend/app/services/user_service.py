from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import models
import schemas
from database import get_db
import uuid
from typing import List
from datetime import datetime
import security

def get_user(email : str, db : Session = Depends(get_db)):
    user = db.query(models.users).filter(models.users.email == email).first()
    return user

def create_user(user : schemas.userBase, db : Session = Depends(get_db)):
    if (get_user(user.email)):
        raise HTTPException(
            status_code=401,
            detail = "User already exists"
        )
    
    hash_password = security.hash_password(user.password)
    new_user = models.users(
        user_id = uuid.uuid4(),
        name = user.name,
        email = user.email,
        hashed_password = hash_password,
        is_active = True,
        role = user.role,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def update_password(email : str, new_password : str ,db : Session = Depends(get_db)):
    #check if user exists
    existing_user = db.query(models.Users).filter(models.Users.email == email).first()

    if not existing_user:
        raise HTTPException(
            status_code=404,
            detail="User does not exist"
        )
    
    #check if new_password == old password
    flag = security.verify_password(new_password,existing_user.hash_password)
    if flag:
        return{
            "message" : "Password is same as the stored password"
        }
    
    existing_user.hash_password = security.hash_password(new_password)
    db.commit()
    db.refresh(existing_user)
    return True


def get_users(db : Session = Depends(get_db)):
    return db.query(models.users).all()

def delete_user(email : str, db : Session = Depends(get_db)):
    if not get_user(email):
        raise HTTPException(
            status_code=404,
            detail = "The user does not exist"
        )
    user = db.query(models.users).filter(models.users.email == email).first()
    db.delete(user)
    db.refresh()
    return True