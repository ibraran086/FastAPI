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
