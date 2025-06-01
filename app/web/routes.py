from fastapi import APIRouter, HTTPException, FastAPI
from app.models.user_models import UserCreate, UserLogin
from app.utils.password import hash_password, verify_password

app = FastAPI()


fake_users_db = {}

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


@app.get('/')
async def products():
    return test_db



@app.post("/register")
def register(user: UserCreate):
    if user.username in fake_users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    fake_users_db[user.username] = {
        "username": user.username,
        "hashed_password": hash_password(user.password)
    }
    return {"msg": "Registered"}

@app.post("/login")
def login(user: UserLogin):
    db_user = fake_users_db.get(user.username)
    if not db_user or not verify_password(user.password, db_user["hashed_password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"msg": "Login successful"}


@app.post("/add")
async def add_products():
    pass


@app.delete("/del")
def delete():
    pass





