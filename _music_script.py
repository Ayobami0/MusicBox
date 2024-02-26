import sys
import os

from shared import Cmd
from pygame.mixer import music, init
from datetime import datetime
from signal import signal, SIGTERM

argv = sys.argv
cmd = Cmd(argv[1])
pos = int(argv[2])

init()

current_playing = 0

def play(now_playin: int = 0):
    global current_playing
    opts = argv[4:]

    if now_playin >= len(opts):
        return

    music.load(opts[now_playin])
    music.play()
    music.set_pos((pos / 1000))
    print("Here")

    current_pos = 0
    while music.get_busy():
        # current_pos = music.get_pos()
        # print(current_pos, end="\r")
        # with open("pause_time", "w") as f:
        #     f.write(f"{current_pos} {now_playin}")
        #     f.flush()
        #     os.fsync(f.fileno())
        current_playing = now_playin
        pass
    play(now_playin + 1)


def __signal_handler(_, __):
    """Function to react to stop/
    kill signal from parent process"""
    with open("pause_time", "w") as f:
        current_pos = music.get_pos()
        f.write(f"{current_pos} {current_playing}")
        f.flush()
        os.fsync(f.fileno())
        exit(0)

signal(SIGTERM, __signal_handler)


if cmd == Cmd.PLAY:
    play()
elif cmd == Cmd.NEXT:
    next()
elif cmd == Cmd.PREV:
    ...
elif cmd == Cmd.STOP:
    ...
elif cmd == Cmd.PAUSE:
    pause()