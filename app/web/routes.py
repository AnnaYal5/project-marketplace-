import os
import sys

from sqlalchemy.orm import Session
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


from fastapi import APIRouter, HTTPException, FastAPI, Depends
from app.models.user_models import UserCreate, UserLogin
from app.utils.password import hash_password, verify_password
import sqlalchemy
from app.models.models import start_db
from app.models.models import User


app = FastAPI()

test_db = [
    {
    'name': "test1",
    "author": "atest1",
    },
    {
    'name': "test2",
    "author": "atest2",
    }

]
auth_app = FastAPI()

app.mount("/auth", auth_app)


@auth_app.post("/register")
async def register(user: UserCreate, db: Session = Depends(start_db)):
    db_user = db.query(User).filter(
        (User.username == user.username) | (User.email == user.email)
    ).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username or email already registered")
    hashed_password = hash_password(user.password)
    n_user = User(username = user.username,
                hashed_password = hashed_password,
                email = user.email)
    db.add(n_user)
    db.commit()
    return {"msg": "Registered"}

@auth_app.post("/login")
async def login(user: UserLogin, db: Session = Depends(start_db)):
    db_user: User = db.query(User).filter(User.username == user.username).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"logged": db_user}


@app.get('/')
async def products():
    return test_db


@app.post("/add")
async def add_products():
    pass


@app.delete("/del")
def delete():
    pass






