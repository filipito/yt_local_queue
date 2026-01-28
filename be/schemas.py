"""Pydantic models for request/response schemas."""

from pydantic import BaseModel


class Song(BaseModel):
    title: str
    artist: str
    duration: int | None = None
    genre: str | None = None
    album: str | None = None


class SearchResult(BaseModel):
    video_id: str
    title: str
    channel: str
    duration: int | None = None
    thumbnail_url: str | None = None


class DownloadRequest(BaseModel):
    video_id: str
    title: str | None = None


class DownloadResponse(BaseModel):
    status: str
    video_id: str
    title: str | None = None
    artist: str | None = None
    duration: int | None = None
    file_path: str | None = None
    error: str | None = None
