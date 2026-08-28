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