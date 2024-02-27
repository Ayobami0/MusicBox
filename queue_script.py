from library.music import Music
import sys
from utils import list_songs
from pygame import mixer

# Remember to deal with multiple spawns.
if __name__ == "__main__":
    # playlist = sys.argv[2:] # Use a substitute below.
    playlist = list_songs(["jingles"])
    playlist += playlist
    music = Music(playlist[0])
    print("This is the first song", playlist[0], len(playlist))
    channel, SOUND_END, _ = music.play(playlist)
    running = True
    while running:
        if channel.get_endevent() == SOUND_END:
            try:
                playlist = playlist[1:]
                channel.queue(mixer.Sound(playlist[0]))
                channel.play(mixer.Sound(playlist[0]))
                print("Here")
            except IndexError:
                running = False
                pass