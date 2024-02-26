from utils import exec
from library.music import Music
from shared import Cmd
from library.config import Config


class MusicQueue:
    __queue: list[Music] = []
    __current: int = -1
    __count: int = 0
    __pause_status = False

    @classmethod
    def add(cls, *songs: Music):
        if cls.__count == 0:
            cls.__current = 0
        cls.__count += len(songs)
        cls.__queue.extend(songs)

    @classmethod
    def next(cls) -> None:
        if cls.__count == 0:
            raise Exception("No Songs in Queue")
        try:
            if Config._script_proc:
                with open("pause_time", "r") as f:
                    r = f.read()
                    print("Here", r.split())
                    cls.__current += int(r.split()[1])
            if cls.__current + 1 >= cls.__count:
                raise Exception("Last Song In Queue")
            cls.__current += 1
            cls.play()
        except IndexError:
            cls.next()

    @classmethod
    def prev(cls) -> None:
        if cls.__count == 0:
            raise Exception("No Songs in Queue")
        try:
            if Config._script_proc:
                with open("pause_time", "r") as f:
                    r = f.read()
                    cls.__current += int(r.split()[1])
            if cls.__current - 1 < 0:
                raise Exception("First Song In Queue")
            cls.__current -= 1

            cls.play()
        except IndexError:
            cls.prev()

    @classmethod
    def list(cls) -> list:
        return cls.__queue

    @classmethod
    def show(cls):
        """Returns a string showing the position of the song queue."""
        return "\n".join(
            [
                f'{m.filename}{" <" if i == cls.__current else ""}'
                for i, m in enumerate(cls.__queue)
            ],
        )

    @classmethod
    def clear(cls):
        cls.__queue.clear()
        cls.__current = -1
        cls.__count = 0

    @classmethod
    def play(cls) -> None:
        if cls.__count == 0:
            raise Exception("No Songs in queue")
        exec(Cmd.PLAY, 0, *[m.filename for m in cls.__queue[cls.__current :]])

    @classmethod
    def pause(cls) -> None:
        cls.__pause_status = True
        if Config._script_proc:
            try:
                with open("pause_time", "r") as f:
                    r = f.read()
                    cls.__pause_time = int(r.split()[0])
            except IndexError:
                cls.pause()
            Config._script_proc.kill()

    @classmethod
    def resume(cls) -> None:
        if cls.__pause_status:
            exec(
                Cmd.PLAY,
                cls.__pause_time,
                *[m.filename for m in cls.__queue[cls.__current :]],
            )
            cls.__pause_status = False
            cls.__pause_time = 0
