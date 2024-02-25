""" This module will contain util functions
that will be used in the program"""
from pathlib import Path
import glob
import datetime
from library.config import Config
from library.music import Music
from subprocess import Popen
import sys
from shared import Cmd


def list_songs(folders: list) -> list:
    """Function to accepts list
    of directories to check for songs
    and list them out"""
    mp3_total_files = []
    for folder in folders:
        # Deal with cases where folder does not exist.
        folder_path = Path(folder)
        if folder_path.exists() and folder_path.is_dir():
            mp3_files = folder_path.glob("*.mp3")
            # mp3_files = glob.glob(str(folder_path / ".{mp3, wav}"))
            mp3_total_files.extend([str(mp3) for mp3 in mp3_files])
    for idx, mp3 in enumerate(mp3_total_files):
        print(idx, mp3)
    return mp3_total_files

def show_metadata(music) -> None:
    from library.music import Music
    """Prints a representation of a music metadata."""
    meta = music.metadata
    length = datetime.timedelta(seconds=int(meta.info.length))
    metadata = f"""
{music.filename}
TITLE  : {meta.get('TIT2')}
ARTIST : {meta.get('TPE1')}
LENGTH : {length}
ALBUM  : {meta.get('TALB')}
TRACK  : {meta.get('TRCK')}
""".strip()
    print(metadata)


def exec(command: Cmd, *args: Path | str):
    if Config._script_proc is not None:
        Config._script_proc.kill()
    cmd = [sys.executable, "_music_script.py", f"{command.value}", *args]
    p = Popen(cmd)
    Config._script_proc = p