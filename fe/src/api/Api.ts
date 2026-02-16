const backendURL: string = 'http://127.0.0.1:8000';

// Unified interface matching backend schema (be/schemas.py)
export interface Song {
  video_id: string;
  title: string;
  channel: string;
  duration: number | null;
  thumbnail_url: string | null;
  // Enriched metadata (null until fetched from music API)
  artist: string | null;
  album: string | null;
}

export async function searchYouTube(query: string): Promise<Song[]> {
  const params = new URLSearchParams({ query });

  const response = await fetch(`${backendURL}/api/youtube-search?${params}`);

  if (!response.ok) {
    throw new Error(`Search failed: ${response.status}`);
  }

  return response.json();
}

// Format seconds as "m:ss" for display
export function formatDuration(seconds: number | null): string {
  if (seconds === null) return '0:00';
  const mins = Math.floor(seconds / 60);
  const secs = seconds % 60;
  return `${mins}:${secs.toString().padStart(2, '0')}`;
}
