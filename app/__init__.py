from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.configurations.api_settings import get_api_settings
from fastapi.staticfiles import StaticFiles
from pathlib import Path


def get_app() -> FastAPI:
    get_api_settings.cache_clear()
    settings = get_api_settings()
    app = FastAPI(**settings.fastapi_kwargs)
    origins = [
        "*"
    ]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.mount(
        "/static",
        StaticFiles(directory=Path(__file__).parent.parent.absolute() / "static"),
        name="static",
    )
    return app
