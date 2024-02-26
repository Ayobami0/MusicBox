import os
import pygame
import cmd
from library.config import Config
from library.queue import MusicQueue
from utils import list_songs
from library.music import Music

# We need this to stop that annoying popup from pygame.
# We would have to shift the console to a different file and call it from
# there.
# So we can set the env var globally. Currently it only affects the script.
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

pygame.mixer.init()


class MusicPlayer(cmd.Cmd):
    def do_play(self, fp):
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

    def do_queue(self, _):
        try:
            song1: pygame.mixer.Sound = Music("./jingles/jingle-bells.mp3")
            song2: pygame.mixer.Sound = Music("./jingles/jingle-bells-rock.mp3")
            song3: pygame.mixer.Sound = Music("./Over_the_Horizon.mp3")
            song4: pygame.mixer.Sound = Music("./jingles/Ayo-by-IF-E.mp3")
            MusicQueue.add(song1, song2, song3, song4)
            return
        except Exception as e:
            print("[ERROR] ", e)
            pass

    def do_next(self, _):
        try:
            MusicQueue.next()
            print(MusicQueue.show())
        except Exception as e:
            print("[ERROR] ", e)
            pass

    def do_prev(self, _):
        """Function to go to the
        previous song on the queue"""
        try:
            MusicQueue.prev()
            print(MusicQueue.show())
        except Exception as e:
            print("[ERROR]", e)

    def do_list(self, line):
        if line == "":
            list_songs(Config.list_dir())
            return
        if line == "queue":
            print([s.filename for s in MusicQueue.list()])
    
    def do_pause(self, _):
        """Function to pause sound"""
        try:
            MusicQueue.pause()
        except Exception as e:
            print("[ERROR]", e)
        # channel.pause()
    
    def do_resume(self, _):
        """Function to resume a
        playing sound"""
        try:
            MusicQueue.resume()
        except Exception as e:
            print("[ERROR]", e)

    def emptyline(self) -> None:
        pass


if __name__ == "__main__":
    Config.load()
    Config.include_dir("library", "jingles", ".")

    MusicPlayer().cmdloop()
