import { Plus, Trash2 } from 'lucide-react';
import { Button } from './ui/button';
import { formatDuration, Song } from '../../api/Api';

interface SongQueueProps {
  queue: Song[];
  selectedSongs: Set<string>;
  onToggleSelect: (songId: string) => void;
  onAddClick: () => void;
  onRemoveSelected: () => void;
  currentSongId: string | null;
}

export function SongQueue({
  queue,
  selectedSongs,
  onToggleSelect,
  onAddClick,
  onRemoveSelected,
  currentSongId,
}: SongQueueProps) {
  return (
    <div className='bg-white rounded-lg shadow-lg p-6'>
      <div className='flex items-center gap-2 mb-4'>
        <Button
          onClick={onAddClick}
          className='bg-green-500 hover:bg-green-600 text-white'
          size='sm'
        >
          <Plus className='size-4 mr-1' />
          Add
        </Button>
        <Button
          onClick={onRemoveSelected}
          disabled={selectedSongs.size === 0}
          variant='destructive'
          size='sm'
        >
          <Trash2 className='size-4 mr-1' />
          Remove
        </Button>
      </div>

      <div className='border rounded-lg overflow-hidden'>
        <div className='bg-gray-50 p-3 border-b'>
          <h3 className='font-semibold'>Queue ({queue.length} songs)</h3>
        </div>

        {queue.length === 0 ? (
          <div className='p-8 text-center text-gray-400'>
            No songs in queue. Click "Add" to get started!
          </div>
        ) : (
          <div className='max-h-[400px] overflow-y-auto'>
            {queue.map((song, index) => (
              <button
                key={`${song.video_id}-${index}`}
                onClick={() => onToggleSelect(song.video_id)}
                className={`w-full text-left p-4 border-b last:border-b-0 transition-colors ${
                  selectedSongs.has(song.video_id)
                    ? 'bg-blue-100 border-blue-200'
                    : 'hover:bg-gray-50'
                } ${
                  currentSongId === song.video_id
                    ? 'bg-purple-50 border-l-4 border-l-purple-500'
                    : ''
                }`}
              >
                <div className='flex items-center justify-between'>
                  <div className='flex-1'>
                    <div className='flex items-center gap-2'>
                      <span className='text-gray-400 text-sm min-w-[24px]'>{index + 1}</span>
                      <div>
                        <p className='font-medium'>{song.title}</p>
                        <p className='text-sm text-gray-600'>{song.artist ?? song.channel}</p>
                      </div>
                    </div>
                  </div>
                  <div className='text-right'>
                    <p className='text-sm text-gray-500'>{formatDuration(song.duration)}</p>
                    {currentSongId === song.video_id && (
                      <p className='text-xs text-purple-600 font-medium'>Now Playing</p>
                    )}
                  </div>
                </div>
              </button>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}
