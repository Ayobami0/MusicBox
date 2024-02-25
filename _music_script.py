import sys

from shared import Cmd
from pygame.mixer import music, init

argv = sys.argv
cmd = Cmd(argv[1])
idx = int(argv[2])

init()


def next():
    if music.get_busy():
        music.stop()


def stop():
    if music.get_busy():
        music.stop()


def play(now_playin: int = 0):
    opts = argv[3:]

    if now_playin >= len(opts):
        return

    music.load(opts[now_playin])
    music.play()

    while music.get_busy():
        pass
    play(now_playin + 1)


if cmd == Cmd.PLAY:
    play(idx)
elif cmd == Cmd.NEXT:
    next()
elif cmd == Cmd.PREV:
    ...
elif cmd == Cmd.STOP:
    ...
elif cmd == Cmd.PAUSE:
    ...
