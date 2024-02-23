from pygame import mixer
from utils import list_songs, show_metadata
from library.music import Music

if __name__ == "__main__":
    mixer.init()

    show_metadata(Music('Over_the_Horizon.mp3'))
    list_songs(["./jingles", "."])
