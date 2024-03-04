import os
from utils import interrupt_handler
from signal import signal, SIGINT

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"


if __name__ == "__main__":
    from console import MusicPlayer
    from library.config import Config
    from library.queue import MusicQueue

    signal(SIGINT, interrupt_handler)
    Config.load()
    try:
        MusicQueue.load()
    except FileNotFoundError:
        print("Creating default queue file...")
    except Exception:
        print("[ERROR] Cannot Parse Queue!!!")
        exit(-1)
    MusicPlayer().cmdloop()
