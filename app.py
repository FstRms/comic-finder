"""Main app module"""

from functools import lru_cache
from typing import Optional

import requests
from fastapi import Depends, FastAPI

from src.config import Settings
from src.formatter import Formatter


@lru_cache()
def get_settings():
    return Settings()


app = FastAPI(
    title="Comic Finder API",
    description="API that retrives comic information from Marvel API",
    version="0.1.0",
)


@app.get("/")
async def home_page():
    """Homepage"""

    return {"message": "Welcome to the Comic Finder API"}


@app.get("/searchComics", status_code=200)
async def search_comics(
    name: Optional[str] = None,
    settings: Settings = Depends(get_settings),
):
    """Search for comics"""

    url = f"{settings.API_URL}characters"
    ts, hash = settings.create_ts_and_hash()
    params = {
        "ts": ts,
        "apikey": settings.PUBLIC_KEY,
        "hash": hash,
    }
    if name:
        params["name"] = name
    response = requests.get(url=url, params=params)
    results = response.json()["data"]["results"]
    if len(results) < 1:
        params.pop("name")
        params["title"] = name
        comic_url = f"{settings.API_URL}comics"
        response = requests.get(url=comic_url, params=params)
        results = response.json()["data"]["results"]
        output = Formatter(results).format_comic()
    else:
        output = Formatter(results).format_character()

    return output
