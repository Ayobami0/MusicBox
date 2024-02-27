import sys
import os

from shared import Cmd, CMD_PROMPT
import pygame
from datetime import datetime

import signal

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
    # Show the currently playing song.
    # \r clears the current line.
    print("\r[NOW PLAYING]", opts[now_playin])
    # pygame.mixer.music.play()
    pygame.mixer.music.play()
    pygame.mixer.music.set_pos((pos / 1000))

    # To fix that issue with command prompt not coming up after play's
    # execution...
    # os.write(0, bytes(CMD_PROMPT, encoding='utf-8'))
    while pygame.mixer.music.get_busy():
        current_pos = pygame.mixer.music.get_pos() + pos
        # print(current_pos, end="\r")
        # with open("pause_time", "w", buffering=1) as f:
        #     f.write(f"{current_pos} {now_playin}")
        #     # f.flush()
        #     # os.fsync(f.fileno())
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

# def __signal_handler(_, __):
#     """Function to react to stop/
#     kill signal from parent process"""
#     with open("pause_time", "w") as f:
#         current_pos = pygame.mixer.music.get_pos()
#         f.write(f"{current_pos} {current_playing}")
#         exit(0)

# signal(SIGTERM, __signal_handler)


if cmd == Cmd.PLAY:
    play()