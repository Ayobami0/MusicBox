import pygame
from pygame import mixer
from mutagen import _util, _file
from pathlib import Path
from shared import Cmd
import subprocess
import sys
import os
from utils import exec


class Music(mixer.Sound):
    mixer.init()
    __channel: mixer.Channel = mixer.find_channel(force=True)
    __playlist: list = []
    metadata: _file.FileType
    __queue = Path("jingles").iterdir() #To be replaced.
    __count = 2

    def __init__(self, file: str) -> None:
        super().__init__(file)

        try:
            meta = _file.File(file)
            if file is None:
                raise Exception('File Format is not supported')
            self.metadata = meta
        except _util.MutagenError:
            # TODO
            ...
        self.path = file
    
    @classmethod
    def play(cls) -> None:
        if cls.__count == 0:
            raise Exception('No Songs in queue')
        exec(Cmd.PLAY, *[str(m) for m in cls.__queue])

    # def play(self, song_list: list[Path] | None) -> mixer.Channel:
    #     """Should set and return channel"""
    #     if song_list is None:
    #         return
    #     sound = mixer.Sound(song_list[0])
    #     self.__channel.play(sound)
    #     print("I should be playing")
    #     SOUND_END = pygame.USEREVENT + 1
    #     self.__channel.set_endevent(SOUND_END)
    #     # song_list.pop()
    #     # if len(song_list) > 0:
    #     #     self.__channel.queue(mixer.Sound(song_list.pop()))
    #     return (self.__channel, SOUND_END, song_list)