import sys

from shared import Cmd
from pygame.mixer import music, init
from subprocess import Popen

argv = sys.argv
# cmd = Cmd(sys.argv[1])

init()

def play(now_playin: int = 0):
    opts = argv[2:]

    if now_playin >= len(opts):
        return

    music.load(opts[now_playin])
    music.play()

    while music.get_busy():
        pass
    play(now_playin + 1)

if Cmd.PLAY == "play":
    play()