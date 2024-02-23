from pathlib import Path
from pygame import mixer
from mutagen import _util, _file


class Music(mixer.Sound):
    channel: mixer.Channel
    metadata: _file.FileType

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

    def play(self) -> None:
        """Should set channel"""
