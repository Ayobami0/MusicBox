from pygame import mixer
from mutagen import _util, _file


class Music(mixer.Sound):
    channel: mixer.Channel
    metadata: _file.FileType

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

    def play(self) -> None:
        """Should set channel"""
