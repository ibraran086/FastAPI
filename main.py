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

