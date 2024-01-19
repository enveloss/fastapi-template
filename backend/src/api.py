from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src import routes

def setup_api(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(routes.router, prefix='/api')
