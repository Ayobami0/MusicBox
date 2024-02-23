from pygame import mixer
from mutagen import _util, _file

mixer.init()  # This would be removed. It should be called in console.


class Music(mixer.Sound):
    channel: mixer.Channel
    metadata: _file.FileType | None

    def __init__(self, file: str) -> None:
        super().__init__(file)

        try:
            self.metadata = _file.File(file)
        except _util.MutagenError:
            # TODO
            ...

    def play(self) -> None:
        """Should set channel"""

# Test: TO BE REMOVED
# with open('test', 'w+') as fp:
#     for k, v in Music('Over_the_Horizon.mp3').metadata.items():
#         print(k, str(v), file=fp)
