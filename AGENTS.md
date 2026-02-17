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
│   ├── services/
│   │   ├── youtube.py      # yt-dlp wrapper logic
│   │   └── library.py      # Local db/file operations
│   └── tests/              # pytest test suite
│       ├── conftest.py     # TestClient fixture
│       ├── test_main.py    # Health check, CORS
│       ├── test_schemas.py # Pydantic model validation
│       ├── test_config.py  # Config sanity checks
│       ├── routers/        # Router endpoint tests (mocked services)
│       └── services/       # Service-layer tests (mocked yt-dlp)
├── fe/                     # React frontend (Vite + Tailwind)
├── .github/workflows/ci.yml # CI: test + lint on every PR
├── pyproject.toml
└── uv.lock
```

## Development Commands

### Backend (FastAPI)
```bash
cd be && uv run uvicorn main:app --reload    # Dev server at http://localhost:8000
uv run pytest                                # Run backend tests
uv run ruff check be/                        # Lint
uv run black --check be/                     # Check formatting
uv run black be/                             # Auto-format
uv run pyright be/                           # Type check
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

# Workflow & Etiquette
## 1. Feature Implementation Process
When asked to implement a feature, strictly follow this sequence:
1.  **Branch**: Create a new git branch with a descriptive name (e.g., `feature/add-login-page`).
2.  **Plan**: Briefly analyze the request and list the files you need to create or modify.
3.  **Implement**: Write the code.
4.  **Verify**: ALWAYS run the **Lint** and **Test** commands defined above before committing. Fix any errors.
5.  **Commit**: Commit changes using a descriptive message (e.g., `feat: implement login page UI`).
6.  **Pull Request**: Use `gh pr create` to open a draft PR with a summary of changes.

## 2. Coding Standards
- **Style**: black
- **Testing**: Add unit tests for new logic.

## 3. Git Rules
-  Do not commit broken code.
-  If checks fail, fix them before pushing.
-  Use `gh` CLI for all PR operations.
