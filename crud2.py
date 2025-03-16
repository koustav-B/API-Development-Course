from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import psycopg2
from psycopg2.extras import RealDictCursor
# Initialize the FastAPI app
app = FastAPI()

# Post model (schema)
class Post(BaseModel):
    id: int
    title: str
    content: str
    published: bool = True  # Default value
    rating: Optional[int] = 4  # Default rating is 4

try:
    conn=psycopg2.connect(host='localhost',database='fastapi',user='Servers',password='csedsatm',cursor_factory=RealDictCursor)
    cursor=conn.cursor()
    print("Creation done")
except Exception as error:
    print("Error",error)

# Temporary database (list to store posts)
posts = [
    Post(id=1, title="Introduction to FastAPI", content="FastAPI is a modern web framework for building APIs.", published=True, rating=5),
    Post(id=2, title="Python Data Structures", content="Learn about lists, dictionaries, and sets in Python.", published=True, rating=4),
    Post(id=3, title="Machine Learning Basics", content="Introduction to ML concepts and algorithms.", published=False, rating=5),
]

# 🏠 Root endpoint
@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI CRUD API"}

# 🟢 CREATE a new post
@app.post("/posts", response_model=Post)
def create_post(post: Post):
    posts.append(post)
    return post

# 🔵 READ all posts
@app.get("/posts", response_model=List[Post])
def get_posts():
    return posts

# 🔵 READ a single post by ID
@app.get("/posts/{post_id}", response_model=Post)
def get_post(post_id: int):
    for post in posts:
        if post.id == post_id:
            return post
    raise HTTPException(status_code=404, detail="Post not found")

# 🟡 UPDATE a post by ID
@app.put("/posts/{post_id}", response_model=Post)
def update_post(post_id: int, updated_post: Post):
    for index, post in enumerate(posts):
        if post.id == post_id:
            posts[index] = updated_post
            return updated_post
    raise HTTPException(status_code=404, detail="Post not found")

# 🔴 DELETE a post by ID
@app.delete("/posts/{post_id}")
def delete_post(post_id: int):
    for index, post in enumerate(posts):
        if post.id == post_id:
            posts.pop(index)
            return {"message": "Post deleted successfully"}
    raise HTTPException(status_code=404, detail="Post not found")
