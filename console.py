from pathlib import Path
import pygame
import cmd
from library.config import Config
from library.queue import MusicQueue
from utils import list_songs

pygame.mixer.init()


class MusicPlayer(cmd.Cmd):

    def do_play(self, line):
        """Play songs in queue, a single song, series of songs or songs
in a directory.
Starts from top of queue or last played song if next or prev is used.

Usage:
    play [filename ... | directory]"""
        try:
            if line == '':
                MusicQueue.play()
                return
            paths = line.split()
            if len(paths) == 1:
                file_or_dir = Path(paths[0])
                if file_or_dir.is_dir():
                    MusicQueue.play_one_or_more(*file_or_dir.glob('*.mp3'))
                else:
                    MusicQueue.play_one_or_more(file_or_dir)
                return
            else:
                MusicQueue.add(*paths)
                return
        except Exception as e:
            print("[ERROR] ", e)
            pass

    def do_queue(self, line: str):
        """Add songs to the main playing queue from a directory,
a list of songs.

Usage:
    queue [filename ... | directory]"""
        try:
            if line == '':
                MusicQueue.add(*[s for s in Config.list_songs()])
                return
            paths = line.split()
            if len(paths) == 1:
                file_or_dir = Path(paths[0])
                if file_or_dir.is_dir():
                    MusicQueue.add(*file_or_dir.glob('*.mp3'))
                MusicQueue.add(file_or_dir)
            else:
                MusicQueue.add(*[Path(file) for file in paths])
            return
        except Exception as e:
            print("[ERROR] ", e)
            pass

    def do_next(self, line):
        """Shift to next song in the main queue.

Usage:
    next"""
        try:
            if line != '':
                print(self.do_next.__doc__)
                return
            MusicQueue.next()
            print(MusicQueue.show())
        except Exception as e:
            print("[ERROR] ", e)
            pass

    def do_prev(self, line):
        """Shift to previous song in the main queue.

Usage:
    prev"""
        try:
            if line != '':
                print(self.do_prev.__doc__)
                return
            MusicQueue.prev()
            print(MusicQueue.show())
        except Exception as e:
            print("[ERROR]", e)

    def do_list(self, line):
        """List songs.

Usage:
    list
    list queue

Options:
    queue   Show only queued songs"""
        if line == "":
            list_songs(Config.list_dir())
            return
        elif line == "queue":
            print([s.filename for s in MusicQueue.list()])
        else:
            print(self.do_list.__doc__)

    def do_pause(self, line):
        """Pause the current playing song in the main queue.

Usage:
    pause"""
        try:
            if line == '':
                MusicQueue.pause()
            else:
                print(self.do_pause.__doc__)
        except Exception as e:
            print("[ERROR]", e)
        # channel.pause()

    def do_resume(self, line):
        """Resume playback of the paused song in the main queue.

Usage:
    resume"""
        try:
            if line == '':
                MusicQueue.resume()
            else:
                print(self.do_resume.__doc__)
        except Exception as e:
            print("[ERROR]", e)

    def emptyline(self) -> None:
        pass
