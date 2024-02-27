import os
import sys

from shared import Cmd
import pygame

argv = sys.argv
cmd = Cmd(argv[1])
pos = int(argv[2])
pygame.init()
current_playing = 0


def play(now_playin: int = 0):
    global current_playing
    opts = argv[3:]

    if now_playin >= len(opts):
        return

    pygame.mixer.music.load(opts[now_playin])
    pygame.mixer.music.play()
    pygame.mixer.music.set_pos((pos / 1000))

    while pygame.mixer.music.get_busy():
        current_pos = pygame.mixer.music.get_pos() + pos
        try:
            fd1 = os.open("pause_time", os.O_WRONLY | os.O_CREAT | os.O_TRUNC)
            val = f"{current_pos} {now_playin}"
            os.write(fd1, val.encode())
        except OSError:
            pass
        finally:
            os.close(fd1)
        current_playing = now_playin
        pass
    play(now_playin + 1)


if cmd == Cmd.PLAY:
    play()
