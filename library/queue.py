from pygame.mixer import Channel
from library.music import Music


class MusicQueue:
    __queue: list[Music] = []
    __current: int = -1
    __count: int = 0

    @classmethod
    def add(cls, *songs: Music):
        if cls.__count == 0:
            cls.__current = 0
        cls.__count += len(songs)
        cls.__queue.extend(songs)

    @classmethod
    def next(cls, channel: Channel) -> None:
        if cls.__count == 0:
            raise Exception("No Songs in Queue")
        if cls.__current + 1 >= cls.__count:
            raise Exception("Last Song In Queue")
        cls.__current += 1
        channel.play(cls.__queue[cls.__current])

    @classmethod
    def prev(cls, channel: Channel) -> None:
        if cls.__count == 0:
            raise Exception("No Songs in Queue")
        if cls.__current - 1 < 0:
            raise Exception("First Song In Queue")
        cls.__current -= 1
        music = cls.__queue[cls.__current]
        channel.play(music)

    @classmethod
    def list(cls) -> list:
        return cls.__queue

    @classmethod
    def clear(cls):
        cls.__queue.clear()
        cls.__current = -1
        cls.__count = 0

    @classmethod
    def play(cls, channel: Channel) -> None:
        if cls.__count == 0:
            raise Exception('No Songs in queue')
        channel.play(cls.__queue[cls.__current])
