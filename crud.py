from sqlalchemy.orm import Session
from models import User
from schemas import *
from fastapi import HTTPException
import models


def create_user(db: Session, user: UserCreate):
    db_user = models.User(name=user.name,fathername=user.fathername,email=user.email,
                          phone=user.phone,age=user.age,degree=user.degree
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user) 
    return db_user


def read_user(db : Session , user_id : int):
    return db.query(User).filter(User.id==user_id).first()

def update_user(db : Session , user_id : int , user : User):
    db_user = db.query(User).filter(User.id==user_id).first()
    db_user.name = user.name
    db_user.fathername = user.fathername
    db_user.email = user.email
    db_user.phone = user.phone
    db_user.age = user.age
    db_user.degree = user.degree
    db.commit()
    db.refresh(db_user)
    return db_user
    
def delete_user(db : Session , user_id : int):
    db_user = db.query(User).filter(User.id==user_id).first()
    if not db_user:
        raise HTTPException(status_code=404 , detail = "User Data Not Found")
    db.delete(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
 
    




