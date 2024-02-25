import os
import sys

from shared import Cmd, CMD_PROMPT
import pygame


argv = sys.argv
cmd = Cmd(argv[1])

pygame.init()


def play(now_playin: int = 0):
    opts = argv[2:]

    if now_playin >= len(opts):
        return

    pygame.mixer.music.load(opts[now_playin])
    # Show the currently playing song.
    # \r clears the current line.
    print("\r[NOW PLAYING]", opts[now_playin])
    pygame.mixer.music.play()

    # To fix that issue with command prompt not coming up after play's
    # execution.
    os.write(0, bytes(CMD_PROMPT, encoding='utf-8'))
    while pygame.mixer.music.get_busy():
        pass
    play(now_playin + 1)


if cmd == Cmd.PLAY:
    play()

