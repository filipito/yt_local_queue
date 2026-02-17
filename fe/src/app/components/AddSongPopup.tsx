import { useState } from 'react';
import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogDescription } from './ui/dialog';
import { Input } from './ui/input';
import { Search, Loader2 } from 'lucide-react';
import { Button } from './ui/button';
import { searchYouTube, formatDuration, Song } from '../../api/Api';

interface AddSongPopupProps {
  isOpen: boolean;
  onClose: () => void;
  onAddSong: (song: Song) => void;
}

export function AddSongPopup({ isOpen, onClose, onAddSong }: AddSongPopupProps) {
  const [searchQuery, setSearchQuery] = useState('');
  const [results, setResults] = useState<Song[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleAddSong = (song: Song) => {
    onAddSong(song);
    setSearchQuery('');
    setResults([]);
    onClose();
  };

  const handleSearch = async () => {
    if (!searchQuery.trim()) return;

    setIsLoading(true);
    setError(null);

    try {
      const data = await searchYouTube(searchQuery);
      setResults(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Search failed');
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter') {
      handleSearch();
    }
  };

  return (
    <Dialog open={isOpen} onOpenChange={onClose}>
      <DialogContent className='max-w-2xl max-h-[600px] flex flex-col'>
        <DialogHeader>
          <DialogTitle>Add Song to Queue</DialogTitle>
          <DialogDescription>Search YouTube for songs to add to your queue.</DialogDescription>
        </DialogHeader>

        <div className='flex gap-2'>
          <div className='relative flex-1'>
            <Search className='absolute left-3 top-1/2 -translate-y-1/2 size-4 text-gray-400' />
            <Input
              placeholder='Search YouTube...'
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              onKeyDown={handleKeyDown}
              className='pl-9'
            />
          </div>
          <Button
            onClick={handleSearch}
            disabled={isLoading || !searchQuery.trim()}
            className='bg-red-600 hover:bg-red-700'
          >
            {isLoading ? <Loader2 className='size-4 animate-spin' /> : 'Search'}
          </Button>
        </div>

        <div className='flex-1 overflow-y-auto space-y-2'>
          {error && <div className='text-center py-4 text-red-500'>{error}</div>}

          {!isLoading && results.length === 0 && !error && (
            <div className='text-center py-8 text-gray-400'>
              Enter a search term and click Search
            </div>
          )}

          {results.map((song) => (
            <button
              key={song.video_id}
              onClick={() => handleAddSong(song)}
              className='w-full text-left p-3 rounded-lg hover:bg-gray-100 transition-colors border border-transparent hover:border-gray-200'
            >
              <div className='flex justify-between items-start'>
                <div className='flex-1'>
                  <p className='font-medium'>{song.title}</p>
                  <p className='text-sm text-gray-600'>{song.artist ?? song.channel}</p>
                </div>
                <span className='text-sm text-gray-500'>{formatDuration(song.duration)}</span>
              </div>
            </button>
          ))}
        </div>
      </DialogContent>
    </Dialog>
  );
}
