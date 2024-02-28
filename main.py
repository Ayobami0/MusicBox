import os
from utils import interrupt_handler
from signal import signal, SIGINT

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"


if __name__ == "__main__":
    from console import MusicPlayer
    from library.config import Config

    signal(SIGINT, interrupt_handler)
    Config.load()
    MusicPlayer().cmdloop()