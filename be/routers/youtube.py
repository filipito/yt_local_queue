"""YouTube search and download endpoints."""

import logging

from fastapi import APIRouter

from schemas import DownloadRequest, DownloadResponse, SearchResult
from services import youtube as youtube_service

router = APIRouter(prefix="/api", tags=["youtube"])

logger = logging.getLogger(__name__)


@router.get("/youtube-search")
async def search_youtube(query: str, max_results: int = 10) -> list[SearchResult]:
    """Search YouTube for videos matching the query."""
    logger.info(f"YouTube search for: {query}")
    results = await youtube_service.search_videos(query, max_results)
    return [SearchResult(**r) for r in results]


@router.post("/youtube-download")
async def download_youtube(request: DownloadRequest) -> DownloadResponse:
    """Download a YouTube video as audio."""
    logger.info(f"Download request for video: {request.video_id}")

    result = await youtube_service.download_audio(request.video_id)

    if result is None:
        return DownloadResponse(
            status="error",
            video_id=request.video_id,
            error="Download failed",
        )

    return DownloadResponse(
        status="success",
        video_id=result["video_id"],
        title=result["title"],
        artist=result["artist"],
        duration=result["duration"],
        file_path=result["file_path"],
    )
