import { useState } from 'react';
import { CurrentSongControl } from './components/CurrentSongControl';
import { SongQueue } from './components/SongQueue';
import { AddSongPopup } from './components/AddSongPopup';
import { Song } from '../api/Api';

export default function App() {
  const [queue, setQueue] = useState<Song[]>([]);
  const [currentSongIndex, setCurrentSongIndex] = useState<number | null>(null);
  const [isPlaying, setIsPlaying] = useState(false);
  const [selectedSongs, setSelectedSongs] = useState<Set<string>>(new Set());
  const [isPopupOpen, setIsPopupOpen] = useState(false);

  const currentSong = currentSongIndex !== null ? queue[currentSongIndex] : null;

  const handleAddSong = (song: Song) => {
    setQueue((prev) => [...prev, song]);

    // Auto-play if this is the first song
    if (queue.length === 0) {
      setCurrentSongIndex(0);
      setIsPlaying(true);
    }
  };

  const handleRemoveSelected = () => {
    const newQueue = queue.filter((song) => !selectedSongs.has(song.video_id));
    setQueue(newQueue);
    setSelectedSongs(new Set());

    // Adjust current song index if needed
    if (currentSongIndex !== null) {
      if (newQueue.length === 0) {
        setCurrentSongIndex(null);
        setIsPlaying(false);
      } else if (currentSongIndex >= newQueue.length) {
        setCurrentSongIndex(0);
      }
    }
  };

  const handleToggleSelect = (songId: string) => {
    setSelectedSongs((prev) => {
      const newSet = new Set(prev);
      if (newSet.has(songId)) {
        newSet.delete(songId);
      } else {
        newSet.add(songId);
      }
      return newSet;
    });
  };

  const handlePlayPause = () => {
    setIsPlaying((prev) => !prev);
  };

  const handleNext = () => {
    if (currentSongIndex !== null && queue.length > 0) {
      setCurrentSongIndex((currentSongIndex + 1) % queue.length);
    }
  };

  const handlePrevious = () => {
    if (currentSongIndex !== null && queue.length > 0) {
      setCurrentSongIndex((currentSongIndex - 1 + queue.length) % queue.length);
    }
  };

  return (
    <div className='min-h-screen bg-gradient-to-br from-gray-10 to-gray-100 p-2'>
      <div className='max-w-4xl mx-auto space-y-2'>
        <CurrentSongControl
          currentSong={currentSong}
          isPlaying={isPlaying}
          onPlayPause={handlePlayPause}
          onNext={handleNext}
          onPrevious={handlePrevious}
        />

        <SongQueue
          queue={queue}
          selectedSongs={selectedSongs}
          onToggleSelect={handleToggleSelect}
          onAddClick={() => setIsPopupOpen(true)}
          onRemoveSelected={handleRemoveSelected}
          currentSongId={currentSong?.video_id || null}
        />

        <AddSongPopup
          isOpen={isPopupOpen}
          onClose={() => setIsPopupOpen(false)}
          onAddSong={handleAddSong}
        />
      </div>
    </div>
  );
}
