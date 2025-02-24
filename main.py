from fastapi import FastAPI
app=FastAPI()

@app.get("/")
def get_user():
    return {"message":"Hello Koustav"}

@app.get("/home")
def get_user():
    return {"mes":"Hello Koustav"}
