from pathlib import Path
from pygame import mixer
from mutagen import _util, _file
from pathlib import Path
from shared import Cmd
import subprocess
import sys
import os
# from utils import exec


class Music(mixer.Sound):
    metadata: _file.FileType
    __queue = Path("jingles").iterdir() #To be replaced.
    __count = 2

    def __init__(self, file: str | Path) -> None:
        super().__init__(file)

        try:
            meta = _file.File(file)
            if file is None:
                raise Exception('File Format is not supported')
            self.metadata = meta
        except _util.MutagenError:
            # TODO
            ...
        if file is Path:
            self.filename = file.name
        else:
            self.filename = file
