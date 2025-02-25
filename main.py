from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True  # Default value is True

@app.post("/createpost")
def create_posts(new_post: Post):
    print("✅ Published Status:", new_post.published)  # Prints `True` or `False`
    return {"data": new_post.dict()}  # Convert to dictionary before returning
