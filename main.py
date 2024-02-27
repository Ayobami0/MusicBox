import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"


if __name__ == "__main__":
    from console import MusicPlayer
    from library.config import Config

    Config.load()
    Config.include_dir("library", "jingles", ".")

    MusicPlayer().cmdloop()
