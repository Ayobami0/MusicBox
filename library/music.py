from pathlib import Path
from pygame import mixer
from mutagen import _file
from pathlib import Path


# Plan to change the implementation for this class, we are not really
# using it to play songs anymore.
class Music(mixer.Sound):
    metadata: _file.FileType

    def __init__(self, file: str | Path) -> None:
        super().__init__(file)

        meta = _file.File(file)
        if meta is None:
            raise Exception('File Format is not supported')
        self.metadata = meta

        if file is Path:
            self.filename = file.name
        else:
            self.filename = file
