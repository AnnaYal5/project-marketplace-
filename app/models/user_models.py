from pydantic import BaseModel, EmailStr

class User(BaseModel):
    email:EmailStr
    password: str
    name: str

class Register(BaseModel):

class Product(BaseModel):
    name:str
