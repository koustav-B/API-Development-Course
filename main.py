from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional  # ✅ Import Optional


app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True# Default value is True
    rating: Optional[int]=4

@app.post("/createpost")
def create_posts(new_post: Post):
    print(new_post.dict())
    print("✅ Rating Status:", new_post.rating)  # Prints `True` or `False`
    return {"data": new_post.dict()}  # Convert to dictionary before returning
