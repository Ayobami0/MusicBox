from music import Music
import sys
from utils import list_songs
from pygame import mixer


# Remember to deal with multiple spawns.
if __name__ == "__main__":
    playlist = sys.argv[2:] # Use a substitute below.
    playlist = list_songs("jingles")
    music = Music(playlist[0])
    channel, SOUND_END, _ = music.play()
    while channel.get_busy():
        if channel.get_end_event() == SOUND_END:
            playlist.pop()
            try:
                channel.queue(mixer.Sound(playlist[1]))
            except IndexError:
                pass