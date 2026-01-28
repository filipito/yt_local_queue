"""Local tracks library endpoints."""

import logging

from fastapi import APIRouter

from schemas import Song

router = APIRouter(prefix="/api", tags=["tracks"])

logger = logging.getLogger(__name__)


@router.get("/tracks")
async def list_tracks() -> list[Song]:
    """List all tracks in the local library."""
    logger.info("Listing tracks")
    # TODO: Implement actual track listing from library service
    return []


@router.get("/tracks/{track_id}")
async def get_track(track_id: str) -> dict:
    """Get details of a specific track."""
    logger.info(f"Getting track: {track_id}")
    # TODO: Implement actual track retrieval
    return {"track_id": track_id, "status": "not_found"}


@router.delete("/tracks/{track_id}")
async def delete_track(track_id: str) -> dict:
    """Delete a track from the local library."""
    logger.info(f"Deleting track: {track_id}")
    # TODO: Implement actual track deletion
    return {"track_id": track_id, "deleted": False}
