"""FastAPI application entry point."""

import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import CORS_ORIGINS
from logging_config import setup_logging
from routers import tracks, youtube

setup_logging()

logger = logging.getLogger(__name__)

app = FastAPI(title="Music App API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(youtube.router)
app.include_router(tracks.router)


@app.get("/")
def read_root():
    """Health check endpoint."""
    logger.info("Root endpoint called")
    return {"Hello": "Flipi"}
