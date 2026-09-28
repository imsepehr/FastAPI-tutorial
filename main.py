from fastapi import FastAPI
from fastapi.responses import HTMLResponse #HTML routes and API routes can be defined in the same FastAPI application. However, it's important to note that HTML routes are typically used for rendering web pages, while API routes are used for returning data in a structured format (like JSON). In this example, we have both types of routes defined in the same FastAPI application.

app = FastAPI()

posts: list[dict] = [
    {
        "id": 1,
        "author": "Corey Schafer",
        "title": "FastAPI is Awesome",
        "content": "This framework is really easy to use and super fast.",
        "date_posted": "April 20, 2025",
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Python is Great for Web Development",
        "content": "Python is a great language for web development, and FastAPI makes it even better.",
        "date_posted": "April 21, 2025",
    },
]

# endpoints or routes
@app.get("/", response_class=HTMLResponse, include_in_schema=False) #include_in_schema=False means that this endpoint will not be included in the OpenAPI schema and dont show in the docs
@app.get("/posts", response_class=HTMLResponse, include_in_schema=False)
def home():
    return f"<h1>{posts[0]['title']}</h1>"

@app.get("/api/posts")
def get_posts():
    return posts