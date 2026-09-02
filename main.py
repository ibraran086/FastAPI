from fastapi import FastAPI
app=FastAPI()

#without venv

@app.get("/")
def home():
    return {"message":"without venv"}


from fastapi import FastAPI
app=FastAPI()
#with venv
@app.get("/")
def home():
    return {"message":"my new website."}
#about router
@app.get("/about")
def about(name,age,designation):
    return {
        "name":name,
        "age":age,
        "Designation":designation
    }

#user router

@app.get("/user")
def user(user_name):
    return user_name

from fastapi import FastAPI
app=FastAPI()

#dynamic router

@app.get("/user/{user_ide}")
def get_user(user_ide):
    return {"user_ide":user_ide}

from fastapi import FastAPI
app=FastAPI()

#query params

@app.get("/user")
def get_user(name:str):
    return {"name":name}

@app.get("/products")
def get_pro(limit:int=10):
    return {"limit":limit}

@app.get("/items")
def get_items(name:str=None,price:int=0):
    return {
        "name":name,
        "price":price
    }

from fastapi import FastAPI
app=FastAPI()

#quary params
@app.get("/user")
def user(person:str):
    return {"person":person}

@app.get("/users")
def users(name:str=None,limit:int=0):
    return {
        "name":name,
        "limit":limit
    }

#POSTAPI

from fastapi import FastAPI
app=FastAPI()

@app.post("/user")
def get_user(name:str,age:int):
    return {
        "name":name,
        "age":age
    }

#real example
from fastapi import FastAPI
app=FastAPI()

@app.post("/create_user")
def create_user(user:dict):
    return {
        "message":"user created",
        "data":user
    }
#pydantic
from fastapi import FastAPI
from pydantic import BaseModel

class person(BaseModel):
    name:str
    age:int
app=FastAPI()
@app.post("/user")
def user(data:person):
    return {
        "message":"hello",
        "data":data
    }

from fastapi import FastAPI
from pydantic import BaseModel
class user(BaseModel):
    name:str
    age:int
app=FastAPI()
@app.post("/data")
def get_data(data:user):
    return {
        "message":"hello pydantic",
        "data":data
    }
from fastapi import FastAPI
from pydantic import BaseModel
class user(BaseModel):
    name:str
    age:int
    email:str
    Address:Address
class Address(BaseModel):
    city:str
    postal_code:int
app=FastAPI()
@app.post("/create_user")
def create_user(user:user):
    return {
        "message":"hi user",
        "data":user
    }
from fastapi import FastAPI
app=FastAPI()
#home router
@app.get("/")
def home():
    return {"message":"hello fastapi"}

from fastapi import FastAPI
app=FastAPI()
#about router
@app.get("/about")
def about():
    return {
        "name":"Ibrar Munir",
        "age":26,
        "data":True
    }
from fastapi import FastAPI
app=FastAPI()
#user router
@app.get("/user/{user_ide}")
def user_ide(user_ide):
    return ("user",user_ide)
from fastapi import FastAPI
app=FastAPI()
#query parameters
@app.get("/create_user")
def create(name:str,age=None,weight=None):
    return {
        "name":name,
        "age":age,
        "weight":weight
    }
from fastapi import FastAPI
app=FastAPI()
#post request
@app.post("/user")
def post(name:str=None,limit:int=10):
    return {
        "name":name,
        "limit":limit
    }
#real example
from fastapi import FastAPI
from pydantic import BaseModel
class user(BaseModel):
    name:str
    age:int
    email:int
    company:company
class company(BaseModel):
    name:str
    address:str
@app.post("/create_user")
def create_user(data:user):
    return data