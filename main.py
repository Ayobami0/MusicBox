import os
from console import MusicPlayer
from library.config import Config


if __name__ == "__main__":
    os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
    Config.load()
    Config.include_dir("library", "jingles", ".")

    MusicPlayer().cmdloop()
