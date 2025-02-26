from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Initialize FastAPI app with metadata for automatic documentation
app = FastAPI(
    title="FastAPI CRUD API",
    description="A simple CRUD API built with FastAPI for managing posts.",
    version="1.0.0",
    contact={
        "name": "Your Name",
        "email": "your.email@example.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
)

# Post model (schema)
class Post(BaseModel):
    id: int
    title: str
    content: str
    published: bool = True  # Default value
    rating: Optional[int] = 4  # Default rating is 4

# Temporary database (list to store posts)
posts = [
    Post(id=1, title="Introduction to FastAPI", content="FastAPI is a modern web framework for building APIs.", published=True, rating=5),
    Post(id=2, title="Python Data Structures", content="Learn about lists, dictionaries, and sets in Python.", published=True, rating=4),
    Post(id=3, title="Machine Learning Basics", content="Introduction to ML concepts and algorithms.", published=False, rating=5),
]

# 🏠 Root endpoint
@app.get("/", summary="Home Page", description="Welcome message for the API.")
def home():
    return {"message": "Welcome to the FastAPI CRUD API"}

# 🟢 CREATE a new post
@app.post("/posts", response_model=Post, summary="Create a new post", description="Adds a new post to the database.")
def create_post(post: Post):
    posts.append(post)
    return post

# 🔵 READ a single post by ID
@app.get("/posts/{post_id}", response_model=Post, summary="Get a post by ID", description="Fetches a post using its unique ID.")
def get_post(post_id: int):
    for post in posts:
        if post.id == post_id:
            return post
    raise HTTPException(status_code=404, detail="Post not found")

# 🔵 READ all posts
@app.get("/posts", response_model=List[Post], summary="Get all posts", description="Returns a list of all posts.")
def get_posts():
    return posts

# 🟡 UPDATE a post by ID
@app.put("/posts/{post_id}", response_model=Post, summary="Update a post", description="Updates a post by its ID.")
def update_post(post_id: int, updated_post: Post):
    for index, post in enumerate(posts):
        if post.id == post_id:
            posts[index] = updated_post
            return updated_post
    raise HTTPException(status_code=404, detail="Post not found")

# 🔴 DELETE a post by ID
@app.delete("/posts/{post_id}", summary="Delete a post", description="Removes a post from the database using its ID.")
def delete_post(post_id: int):
    for index, post in enumerate(posts):
        if post.id == post_id:
            posts.pop(index)
            return {"message": "Post deleted successfully"}
    raise HTTPException(status_code=404, detail="Post not found")
