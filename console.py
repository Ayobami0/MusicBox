from pathlib import Path
import pygame
import cmd
from library.config import Config
from library.queue import MusicQueue
from utils import list_songs, show_metadata, split_tokens

pygame.mixer.init()


class MusicPlayer(cmd.Cmd):
    def do_play(self, line):
        """Play songs in queue, a single song,\
 series of songs or songs in a directory.
        \rStarts from top of queue or last played song if next or prev is used.

        \rUsage:
            \r\tplay [filename ... | directory]"""
        try:
            if line == "":
                MusicQueue.play()
                return
            paths = line.split()
            if len(paths) == 1:
                file_or_dir = Path(paths[0])
                if not file_or_dir.exists():
                    raise Exception(
                        f"No such file or directory: {file_or_dir}",
                    )
                if file_or_dir.is_dir():
                    MusicQueue.play_one_or_more(*file_or_dir.glob("*.mp3"))
                else:
                    MusicQueue.play_one_or_more(file_or_dir)
                return
            else:
                # MusicQueue.clear ## Overwrite queue.
                MusicQueue.add(*paths)
                # MusicQueue.play()
                return
        except Exception as e:
            print("[ERROR] ", e)
            pass

    def do_queue(self, line: str):
        """Add songs to the main playing queue\
 from a directory, a list of songs.

        \rUsage:
            \r\tqueue [preset-index ... | filename ... | directory]\
 [overwrite]"""
        try:
            if line == "":
                MusicQueue.add(*[s for s in Config.list_songs()])
                return
            paths = line.split()  # Queue with integer list.
            if len(paths) == 1 and not paths[0].isdigit():
                file_or_dir = Path(paths[0])
                if not file_or_dir.exists():
                    raise Exception(
                        f"No such file or directory: {file_or_dir}",
                    )
                if file_or_dir.is_dir():
                    MusicQueue.add(*file_or_dir.glob("*.mp3"))
                MusicQueue.add(file_or_dir)
            else:
                preset_indexes = set()
                for f in paths:
                    if f.isdigit():
                        preset_indexes.add(int(f))
                    elif not f.isdigit() and len(preset_indexes) != 0:
                        raise Exception(
                            """Arguments must be either preset-indexes,\
 files or directory"""
                        )
                if len(preset_indexes) != 0:
                    MusicQueue.add(
                        *(Config.list_songs()[i] for i in preset_indexes),
                    )
                else:
                    MusicQueue.add(*(Path(file) for file in paths))
            return
        except Exception as e:
            print("[ERROR] ", e)
            pass

    def do_next(self, line):
        """Shift to next song in the main queue.

        \rUsage:
            \r\tnext"""
        try:
            if line != "":
                print(self.do_next.__doc__)
                return
            MusicQueue.next()
            print(MusicQueue.show())
        except Exception as e:
            print("[ERROR]", e)
            pass

    def do_prev(self, line):
        """Shift to previous song in the main queue.

        \rUsage:
            \r\tprev"""
        try:
            if line != "":
                print(self.do_prev.__doc__)
                return
            MusicQueue.prev()
            print(MusicQueue.show())
        except Exception as e:
            print("[ERROR]", e)

    def do_list(self, line):
        """List songs.

        \rUsage:
            \r\tlist
            \r\tlist queue

        \rOptions:
            \r\tqueue   Show only queued songs"""
        if line == "":
            list_songs(Config.list_dir())
            return
        elif line == "queue":
            for i, s in enumerate(MusicQueue.list()):
                print(i, s)
        else:
            print(self.do_list.__doc__)

    def do_pause(self, line):
        """Pause the current playing song in the main queue.

        \rUsage:
            \r\tpause"""
        try:
            if line == "":
                MusicQueue.pause()
            else:
                print(self.do_pause.__doc__)
        except Exception as e:
            print("[ERROR]", e)
        # channel.pause()

    def do_stop(self, line):
        """Stop the current playing song in the main queue.
        \rBehaviour is exactly like pause.

        \rUsage:
            \r\tstop"""
        try:
            if line == "":
                MusicQueue.pause()
            else:
                print(self.do_pause.__doc__)
        except Exception as e:
            print("[ERROR]", e)
        # channel.pause()

    def do_resume(self, line):
        """Resume playback of the paused song in the main queue.

        \rUsage:
            \r\tresume"""
        try:
            if line == "":
                MusicQueue.resume()
            else:
                print(self.do_resume.__doc__)
        except Exception as e:
            print("[ERROR]", e)

    def do_info(self, line):
        """Check the info of a music file, or the currently playing song.

        \rUsage:
            \r\tinfo <filename> | <queue <song-number | playing>

        \rOptions:
            \r\tqueue playing           Shows the info of the currently playing song.
            \r\tqueue <song-number>     Shows the info of a song in queue by it's index.
        """
        try:
            if line == "" or len(line.split()) > 2:
                print(self.do_info.__doc__)
                return
            cmd = line.split()
            if cmd[0] == "queue":
                if len(cmd) < 2:
                    print(self.do_info.__doc__)
                    return
                try:
                    if cmd[1] == "playing":
                        try:
                            show_metadata(MusicQueue.get_current())
                        except IndexError:
                            raise Exception("No song is currently playing")
                    else:
                        song = MusicQueue.list()[int(cmd[1])]
                        show_metadata(song)
                except IndexError:
                    raise Exception(f"{cmd[1]} is not part of the queue.")
            else:
                show_metadata(Path(cmd[0]))

        except Exception as e:
            print("[ERROR]", e)

    def do_preset(self, line):
        """preset sets the directories that MusicBox uses to search for songs.
        \rBy default, MusicBox presets the current directory and the jingles directory.

        \rUsage:
             \r\tpreset <dir1> <dir2> ... [overwrite]

        \rOptions:
            \r\t<dir> ...               This will append the directories to existing search list.
            \r\t<dir> ... overwrite     This will overwite the existing search list with new list.

        \rNOTE:
            \r\t1. overwrite will only overwrite, if at least one of the directories specified is valid.
            \r\t2. Each directory is written as the the relative or absolute path.
            \r\t3. Double quotes around any given directory counts as one. e.g "Dell 7490"
        """
        try:
            if line == "" or line.split()[0] == "overwrite":
                if line.split()[0] == "overwrite":
                    raise Exception(
                        "preset takes at least a directory before `overwrite`"
                    )
                print(self.do_preset.__doc__)
                return
            overwrite = False
            dirs = split_tokens(line)
            invalid_paths = set()
            valid_paths = set()
            if dirs[-1] == "overwrite":
                dirs = dirs[:-1]
                overwrite = True
            for dir in dirs:
                if Path(dir).is_dir():
                    # Config.include_dir(dir)
                    valid_paths.add(dir)
                else:
                    invalid_paths.add(dir)
            if len(valid_paths) > 0:
                if overwrite:
                    Config.clear_list()
                Config.include_dir(*valid_paths)
                print("The following directories have been added for search:")
                print("\t----->  ", *valid_paths)
            if len(invalid_paths) > 0:
                print(
                    """\r
                      \rThe following are not directories and could not be added:"""
                )
                print("\t------->", *invalid_paths)

        except Exception as e:
            print("[ERROR]", e)

    def do_search_list(self, line):
        """This shows the preset directories that MusicBox uses to search for songs.

        \rUsage: search_list
        """
        try:
            if line != "":
                raise Exception(
                    """search_list does not take additional options
                    \rUsage: search_list
                    """
                )
            print(*(Config.list_dir()))
        except Exception as e:
            print("[ERROR]", e)
    
    def do_reset(self, line):
        """reset the existing queue that MusicBox is using to play"""
        try:
            MusicQueue.clear()
        except Exception as e:
            print("[ERROR]", e)

    def emptyline(self) -> None:
        pass

    def do_exit(self, _):

        """Used to exit MusicBox.
        \rUsage: exit

        \rAnything after exit is not taken into consideration.
        """
        if Config._script_proc is not None:
            Config._script_proc.kill()
            Config._script_proc = None
        print(
        """\n\nGood Bye to MusicBox v1.0.\n
        \r-->  Developed by OLUDEMI Ayobami and AKINGBENI David using Python.
        \r-->  Done as ALX Foundations Portfolio Project.
        \r-->  To see more information about us, check out\
 our GitHub profile using
        \r|
        \r|->  https://github.com/Ayobami0      (Ayobami)
        \r|->  https://github.com/deelight-del/ (David)
          """)
        exit(0)
    
    def do_EOF(self, _):
        exit(0)

    def default(self, line: str) -> None:
        print(f"[ERROR] Invalid command: {line}")
        print()
        self.do_help("")
