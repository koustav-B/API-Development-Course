from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_user():
    return {"message": "Hello Koustav"}

@app.get("/home")
def get_home():
    return {"mes": "Hello Koustav"}

@app.post("/createpost")
def create_posts():
    return {"message": "Post created successfully"}
