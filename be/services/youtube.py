"""YouTube/yt-dlp wrapper service."""

import asyncio
import logging
import os
from pathlib import Path

import yt_dlp

from config import TRACKS_PATH

logger = logging.getLogger(__name__)


def _search_sync(query: str, max_results: int = 10) -> list[dict]:
    """Synchronous search implementation."""
    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
        "extract_flat": "in_playlist",
    }

    search_query = f"ytsearch{max_results}:{query}"

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(search_query, download=False)

    if not result or "entries" not in result:
        return []

    videos = []
    for entry in result["entries"]:
        if entry is None:
            continue
        videos.append(
            {
                "video_id": entry.get("id", ""),
                "title": entry.get("title", ""),
                "channel": entry.get("channel") or entry.get("uploader", ""),
                "duration": entry.get("duration"),
                "thumbnail_url": entry.get("thumbnail"),
            }
        )

    return videos


async def search_videos(query: str, max_results: int = 10) -> list[dict]:
    """Search YouTube for videos."""
    logger.info(f"Searching YouTube for: {query}")
    loop = asyncio.get_event_loop()
    results = await loop.run_in_executor(None, _search_sync, query, max_results)
    logger.info(f"Found {len(results)} results")
    return results


def _download_sync(video_id: str, output_dir: str) -> dict | None:
    """Synchronous download implementation."""
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    output_template = os.path.join(output_dir, "%(id)s.%(ext)s")
    url = f"https://www.youtube.com/watch?v={video_id}"

    # Try with ffmpeg conversion first
    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
        "outtmpl": output_template,
        "quiet": True,
        "no_warnings": True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
        ext = "mp3"
    except Exception as e:
        if "ffmpeg" in str(e).lower():
            # Fallback: download without conversion
            logger.warning("ffmpeg not available, downloading raw audio")
            ydl_opts = {
                "format": "bestaudio/best",
                "outtmpl": output_template,
                "quiet": True,
                "no_warnings": True,
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
            ext = info.get("ext", "webm")
        else:
            raise

    if not info:
        return None

    file_path = os.path.join(output_dir, f"{video_id}.{ext}")

    return {
        "video_id": video_id,
        "title": info.get("title", ""),
        "artist": info.get("channel") or info.get("uploader", ""),
        "duration": info.get("duration"),
        "file_path": file_path,
    }


async def download_audio(video_id: str, output_dir: str | Path | None = None) -> dict | None:
    """Download audio from a YouTube video.

    Returns metadata dict with file_path on success, None on failure.
    """
    if output_dir is None:
        output_dir = str(TRACKS_PATH)
    else:
        output_dir = str(output_dir)

    logger.info(f"Downloading video {video_id} to {output_dir}")

    loop = asyncio.get_event_loop()
    try:
        result = await loop.run_in_executor(None, _download_sync, video_id, output_dir)
        if result:
            logger.info(f"Downloaded: {result['title']}")
        return result
    except Exception as e:
        logger.error(f"Download failed for {video_id}: {e}")
        return None
