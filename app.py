"""Main app module"""

from fastapi import FastAPI

app = FastAPI(
    title="Comic Finder API",
    description="API that retrives comic information from Marvel API",
    version="0.1.0",
)


@app.get("/")
async def home_page():
    """Homepage"""

    return {"message": "Welcome to the Comic Finder API"}
