"""Shared constants beteween main program and scripts.

Define constants used in both programs
"""
from enum import Enum


class Cmd(Enum):
    PLAY = "play"
    STOP = "stop"
    PAUSE = "pause"
    NEXT = "next"
    PREV = "prev"


CMD_PROMPT = "(Cmd) "
