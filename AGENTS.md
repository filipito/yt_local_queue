# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Music app that downloads tracks from YouTube (yt-dlp), archives locally, and plays them.

## Project Structure

```
youtube_fe/
├── be/                     # Python backend (FastAPI)
│   ├── main.py             # App creation, middleware, router registration
│   ├── config.py           # Settings (CORS origins, paths, db config)
│   ├── schemas.py          # Pydantic models (Song, SearchResult, DownloadRequest)
│   ├── logging_config.py   # Logging setup
│   ├── routers/
│   │   ├── youtube.py      # /api/youtube-search, /api/youtube-download
│   │   └── tracks.py       # /api/tracks (list, get, delete)
│   └── services/
│       ├── youtube.py      # yt-dlp wrapper logic
│       └── library.py      # Local db/file operations
├── fe/                     # React frontend (Vite + Tailwind)
├── pyproject.toml
└── uv.lock
```

## Development Commands

### Backend (FastAPI)
```bash
cd be && uv run uvicorn main:app --reload    # Dev server at http://localhost:8000
black be/                                      # Format
ruff be/                                       # Lint
```

### Frontend (React/Vite)
```bash
cd fe && npm run dev     # Dev server at http://localhost:3000
cd fe && npm run build   # Production build
```

## Tech Stack

- **Backend**: Python 3.14+, FastAPI, yt-dlp, uv
- **Frontend**: React 18, Vite, Tailwind CSS 4, MUI, Radix UI, Lucide icons
- **Figma**: https://www.figma.com/design/q0nGKUFiYfcYgC5ln7Efg2/Music-Player-App

## API Routes
- `GET /api/youtube-search?query=` - Search YouTube
- `POST /api/youtube-download` - Download video as audio
- `GET|DELETE /api/tracks[/{id}]` - Manage local library

## Git
-  Branch naming: <FIX/FEATURE>_<short_description>_claude
-  when finished with something, make a pull request, use slash command /pr_preparation beforehand
