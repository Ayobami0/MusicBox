import pygame
import cmd
from library.config import Config
from library.queue import MusicQueue
from utils import list_songs
from library.music import Music

pygame.mixer.init()


class MusicPlayer(cmd.Cmd):

    def do_play(self, fp):
        """Play songs in queue, a single song or series of songs.
Starts from top of queue or last played song if next or prev is used.

Usage:
    play [filename ...]"""
        try:
            if fp != "":
                song: pygame.mixer.Sound = Music(fp)
                MusicQueue.add(song)
                MusicQueue.play()
                print("[PLAYING]", fp)
            MusicQueue.play()
            print("[PLAYING] Queue")
        except Exception as e:
            print("[ERROR] ", e)
            pass

    def do_queue(self, line: str):
        """Add songs to the main playing queue.

Usage:
    queue <filename> ...
    queue <directory>"""
        try:
            if line == '':
                return
            paths = line.split()
            if len(paths) == 1:
                MusicQueue.add()
            else:
                MusicQueue.add(*[Music(file) for file in paths])
            return
        except Exception as e:
            print("[ERROR] ", e)
            pass

    def do_next(self, _):
        """Shift to next song in the main queue.

Usage:
    next"""
        try:
            MusicQueue.next()
            print(MusicQueue.show())
        except Exception as e:
            print("[ERROR] ", e)
            pass

    def do_prev(self, _):
        """Shift to previous song in the main queue.

Usage:
    prev"""
        try:
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
        if line == "queue":
            print([s.filename for s in MusicQueue.list()])

    def do_pause(self, _):
        """Pause the current playing song in the main queue.

Usage:
    pause"""
        try:
            MusicQueue.pause()
        except Exception as e:
            print("[ERROR]", e)
        # channel.pause()

    def do_resume(self, _):
        """Resume playback of the paused song in the main queue.

Usage:
    resume"""
        try:
            MusicQueue.resume()
        except Exception as e:
            print("[ERROR]", e)

    def emptyline(self) -> None:
        pass
