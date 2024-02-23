from pygame import mixer
from mutagen import _util, _file

mixer.init()  # This would be removed. It should be called in console.


class Music(mixer.Sound):
    channel: mixer.Channel
    info: _file.FileType | None

    def __init__(self, file: str) -> None:
        super().__init__(file)

        try:
            self.info = _file.File(file)
        except _util.MutagenError:
            # TODO
            ...

    def play(self) -> None:
        """Should set channel"""


print(Music('Over_the_Horizon.mp3').info)
