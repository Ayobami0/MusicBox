import cmd
from library.music import Music
from utils import list_songs
import subprocess
import pygame


class MusicBox(cmd.Cmd):
    """Test console."""
    def do_play(self, line):
            try:
                # playlist = list_songs(["jingles"])
                # print(playlist)
                # music = Music(playlist[0])
                Music.play()
                # command = ["python", "queue_script.py", "fill", "filler"]
                # subprocess.Popen(command)
                print("Am I here")
                return
            except Exception as e:
                print("Error occurred", e)
                pass

if __name__ == "__main__":
     MusicBox().cmdloop()