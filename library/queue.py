from pathlib import Path
from utils import exec
from shared import Cmd
from library.config import Config


class MusicQueue:
    __queue: list[Path] = []
    __current: int = -1
    __count: int = 0
    __pause_status = False

    @classmethod
    def add(cls, *songs: Path):
        for s in songs:
            if not s.exists():
                raise Exception(f'File {s.name} does not exists')
            if not s.is_file:
                raise Exception(f'File {s.name} is a directory')
        if cls.__count == 0:
            cls.__current = 0
        cls.__count += len(songs)
        cls.__queue.extend(songs)
    
    def clear(cls):
        """Clear all songs in queue"""
        cls.__queue.clear()

    @classmethod
    def next(cls) -> None:
        if cls.__count == 0:
            raise Exception("No Songs in Queue")
        if cls.__current + 1 >= cls.__count:
            raise Exception("Last Song In Queue")
        try:
            if Config._script_proc is not None:    
                with open("pause_time", "r", encoding="utf-8") as f:
                    r = f.read()
                    print("Here", r.split()) ##
                    cls.__current += int(r.split()[1])
            cls.__current += 1
            cls.play()
        except IndexError:
            cls.next()

    @classmethod
    def prev(cls) -> None:
        if cls.__count == 0:
            raise Exception("No Songs in Queue")
        if cls.__current - 1 < 0:
            raise Exception("First Song In Queue")
        try:
            if Config._script_proc is not None:
                with open("pause_time", "r") as f:
                    r = f.read()
                    cls.__current += int(r.split()[1])
            cls.__current -= 1

            cls.play()
        except IndexError:
            cls.prev()

    @classmethod
    def list(cls) -> list:
        return cls.__queue

    @classmethod
    def get_current(cls) -> Path:
        return cls.__queue[cls.__current]

    @classmethod
    def show(cls):
        """Returns a string showing the position of the song queue."""
        return "\n".join(
            [
                f'{p.name}{" <" if i == cls.__current else ""}'
                for i, p in enumerate(cls.__queue)
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
        cls.play_one_or_more(
            *[p for p in cls.__queue[cls.__current:]],
            start_pos=0
        )

    @classmethod
    def pause(cls) -> None:
        cls.__pause_status = True
        if Config._script_proc is not None:
            try:
                with open("pause_time", "r") as f:
                    r = f.read()
                    cls.__pause_time = int(r.split()[0])
                    cls.__current += int(r.split()[1])
            except IndexError:
                cls.pause()
            Config._script_proc.kill()
            Config._script_proc = None

    @classmethod
    def resume(cls) -> None:
        if cls.__pause_status:
            cls.play_one_or_more(
                *[p for p in cls.__queue[cls.__current:]],
                start_pos=cls.__pause_time
            )
            cls.__pause_status = False
            cls.__pause_time = 0

    @staticmethod
    def play_one_or_more(*paths, start_pos=0):
        """
        A static helper method that provides an
        interface to the exec function"""
        exec(Cmd.PLAY, start_pos, *paths)
