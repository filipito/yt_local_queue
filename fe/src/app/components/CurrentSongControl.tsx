import { Play, Pause, SkipBack, SkipForward } from 'lucide-react';
import { Button } from './ui/button';
import { Song } from '../../api/Api';

interface CurrentSongControlProps {
  currentSong: Song | null;
  isPlaying: boolean;
  onPlayPause: () => void;
  onNext: () => void;
  onPrevious: () => void;
}

export function CurrentSongControl({
  currentSong,
  isPlaying,
  onPlayPause,
  onNext,
  onPrevious,
}: CurrentSongControlProps) {
  return (
    <div className='bg-gradient-to-r from-purple-500 to-blue-500 p-6 rounded-lg shadow-lg'>
      <div className='flex items-center justify-between mb-4'>
        <div className='flex-1'>
          {currentSong ? (
            <>
              <h2 className='text-white text-2xl mb-1'>{currentSong.title}</h2>
              <p className='text-purple-100'>{currentSong.artist ?? currentSong.channel}</p>
            </>
          ) : (
            <>
              <h2 className='text-white text-2xl mb-1'>No song playing</h2>
              <p className='text-purple-100'>Add songs to the queue to get started</p>
            </>
          )}
        </div>
      </div>

      <div className='flex items-center justify-center gap-4'>
        <Button
          variant='ghost'
          size='icon'
          onClick={onPrevious}
          disabled={!currentSong}
          className='size-12 rounded-full bg-white/20 hover:bg-white/30 text-white disabled:opacity-50'
        >
          <SkipBack className='size-6' />
        </Button>

        <Button
          variant='ghost'
          size='icon'
          onClick={onPlayPause}
          disabled={!currentSong}
          className='size-16 rounded-full bg-white hover:bg-white/90 text-purple-600 disabled:opacity-50'
        >
          {isPlaying ? <Pause className='size-8' /> : <Play className='size-8 ml-1' />}
        </Button>

        <Button
          variant='ghost'
          size='icon'
          onClick={onNext}
          disabled={!currentSong}
          className='size-12 rounded-full bg-white/20 hover:bg-white/30 text-white disabled:opacity-50'
        >
          <SkipForward className='size-6' />
        </Button>
      </div>
    </div>
  );
}
