from pygame import mixer
from library.config import Config
from library.queue import MusicQueue
from utils import list_songs
from library.music import Music
import cmd

mixer.init()


class MusicPlayer(cmd.Cmd):
    channel = mixer.find_channel()

    def do_play(self, fp):
        try:
            if fp != "":
                song: mixer.Sound = Music(fp)
                MusicQueue.add(song)
                MusicQueue.play(channel)
                print("[PLAYING]", fp)

            MusicQueue.play(channel)
            print("[PLAYING] Queue")
            return
        except Exception as e:
            print("[ERROR] ", e)
            pass

    def do_queue(self, _):
        try:
            song1: mixer.Sound = Music("./jingles/jingle-bells.mp3")
            song2: mixer.Sound = Music("./jingles/jingle-bells-rock.mp3")
            song3: mixer.Sound = Music("./Over_the_Horizon.mp3")
            MusicQueue.add(song1, song2, song3)
            return
        except Exception as e:
            print("[ERROR] ", e)
            pass

    def do_next(self, _):
        try:
            channel.stop()
            MusicQueue.next(channel)
        except Exception as e:
            print("[ERROR] ", e)
            pass

    def do_list(self, line):
        if line == "":
            list_songs(config.list_dir())
            return
        if line == "queue":
            print([s.filename for s in MusicQueue.list()])


if __name__ == "__main__":
    config = Config()
    config.include_dir("library", "jingles", ".")
    channel = mixer.find_channel()

    MusicPlayer().cmdloop()
