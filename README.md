# YouTube Local Queue (yt_local_queue)

A modern web application designed for managing a local queue of YouTube audio tracks. Search for your favorite videos, download them as high-quality audio, and organize them into a seamless playback queue.

## Project Focus

This project focuses on providing a **self-hosted, local-first alternative** to cloud-based music services. It bridges the gap between YouTube's vast library and local audio management by automating the download and metadata extraction process.

### Key Objectives:
- **Fast Discovery**: Integrated YouTube search for quick track finding.
- **Local Storage**: Automatically download and convert videos to MP3 for offline access.
- **Modern UX**: A slick, responsive frontend built with React and Tailwind CSS.
- **Queue-Centric**: Focused on dynamic playlist/queue management for a continuous listening experience.

## Technology Stack

### Backend
- **Framework**: [FastAPI](https://fastapi.tiangolo.com/) (Python)
- **Downloader**: [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- **Processing**: FFmpeg (used via `yt-dlp` for MP3 conversion)
- **API Design**: RESTful endpoints for search, download, and library management.

### Frontend
- **Framework**: [React](https://reactjs.org/) with [TypeScript](https://www.typescriptlang.org/)
- **Build Tool**: [Vite](https://vitejs.dev/)
- **Styling**: [Tailwind CSS](https://tailwindcss.com/)
- **Components**: [Radix UI](https://www.radix-ui.com/), [Material UI Icons](https://mui.com/material-ui/material-icons/)
- **Animations**: [Framer Motion](https://www.framer.com/motion/)

## Features (Current State)
- [x] **YouTube Search**: Search videos directly from the UI.
- [x] **Audio Downloading**: One-click download with automatic MP3 conversion.
- [x] **Dynamic Queue**: Add and remove tracks from a live queue.
- [x] **Modern UI**: Dark-themed, responsive design with smooth transitions.

## What's Missing / Roadmap

The project is currently in early development. The following features are identified as missing or partially implemented:

- [ ] **Persistent Library**: The `tracks` API is currently a placeholder. Implementing a database (like SQLite or PostgreSQL) to track downloaded files and metadata is a priority.
- [ ] **Actual Audio Playback**: The frontend UI for playback is ready, but the underlying audio streaming and controls (HTML5 Audio integration) need to be implemented.
- [ ] **Metadata Editing**: Ability to edit ID3 tags (Artist, Album, Genre) for downloaded tracks.
- [ ] **Playlist Support**: Create and save multiple playlists.
- [ ] **Search History**: Keep track of previous searches for quick access.
- [ ] **User Authentication**: Secure your local library with user accounts.
- [ ] **Backend-to-Frontend Streaming**: Efficiently serve audio files from the `be/storage/tracks` directory to the browser.

## Getting Started

### Prerequisites
- Python 3.14+
- Node.js 18+
- FFmpeg (required for MP3 conversion)
- [uv](https://docs.astral.sh/uv/) (Python package manager)

### Setup

1. **Backend**:
   ```bash
   uv sync --dev                                 # Install dependencies
   cd be && uv run uvicorn main:app --reload     # Dev server at http://localhost:8000
   ```

2. **Frontend**:
   ```bash
   cd fe && npm install
   npm run dev                                    # Dev server at http://localhost:3000
   ```

## Development

```bash
uv run pytest                    # Run backend tests
uv run ruff check be/            # Lint
uv run black --check be/         # Check formatting
uv run pyright be/               # Type check
```

CI runs these checks automatically on every pull request via GitHub Actions.

## License
MIT
