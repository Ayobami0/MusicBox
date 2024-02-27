from utils import exec
from library.music import Music
from shared import Cmd


class MusicQueue:
    __queue: list[Music] = []
    __current: int = -1
    __count: int = 0
    __pause_status = False
    ## __pause_time = 0

    @classmethod
    def add(cls, *songs: Music):
        if cls.__count == 0:
            cls.__current = 0
        cls.__count += len(songs)
        cls.__queue.extend(songs)
        
    @classmethod
    def next(cls) -> None: 
        from library.config import Config
        if cls.__count == 0:
            raise Exception("No Songs in Queue")
        ### Update the __current from runnig file from script.
        try:
            if Config._script_proc:    
                with open("pause_time", "r", encoding="utf-8") as f:
                    r = f.read()
                    print("Here", r.split())
                    cls.__current += int(r.split()[1])
            #----------------------------------------->
            if cls.__current + 1 >= cls.__count:
                raise Exception("Last Song In Queue")
            cls.__current += 1
            cls.play()
        except IndexError:
            cls.next()

    @classmethod
    def prev(cls) -> None:
        from library.config import Config
        if cls.__count == 0:
            raise Exception("No Songs in Queue")
        ## Update __current from running file, Script.
        try:
            if Config._script_proc:
                with open("pause_time", "r") as f:
                    r = f.read()
                    cls.__current += int(r.split()[1])
            #----------------------------------------->
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
        """ Returns a string showing the position of the song queue."""
        return "\n".join(
            [
                # displays an arrow after the song to show the position
                # on the queue
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
        exec(Cmd.PLAY, 0, *[m.filename for m in cls.__queue[cls.__current:]])
    
    @classmethod
    def pause(cls) -> None:
        from library.config import Config
        import signal

        cls.__pause_status = True
        if Config._script_proc:
            try:
                with open("pause_time", "r") as f:
                    r = f.read()
                    print(r.split())
                    cls.__pause_time = int(r.split()[0])
            except IndexError:
                cls.pause()
            Config._script_proc.kill()
    
    @classmethod
    def resume(cls) -> None:
        if cls.__pause_status:
            from library.config import Config
            import signal
            print("Here")
            with open("pause_time", "r") as f:
                r = f.read()
            exec(
                Cmd.PLAY,
                cls.__pause_time,
                *[m.filename for m in cls.__queue[cls.__current:]]
                )
            print(Config._script_proc.args)
            cls.__pause_status = False
            cls.__pause_time = 0
