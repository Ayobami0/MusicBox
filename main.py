from pygame import mixer
from library.config import Config
from utils import list_songs, show_metadata
from library.music import Music

if __name__ == "__main__":
    mixer.init()

    config = Config()
    print(config.list_dir())
    config.include_dir('library', 'jingles', '.')
    print(config.list_dir())
    for path in config.list_dir():
        list_songs(config.list_dir())
        for music in [Music(song) for song in path.glob('*.mp3')]:
            show_metadata(music)
