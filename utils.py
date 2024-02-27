""" This module will contain util functions
that will be used in the program"""
from pathlib import Path
import glob
import datetime
from mutagen import _file

from library.config import Config
from subprocess import Popen, PIPE

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


def show_metadata(song: Path) -> None:
    """Prints a representation of a song metadata."""
    if not song.is_file():
        raise Exception(f'{song} is not a valid file')
    meta = _file.File(song)
    if meta is None:
        raise Exception(f'{song} is not a valid song file')
    length = datetime.timedelta(seconds=int(meta.info.length))
    metadata = f"""
===============================
{song}
TITLE  : {meta.get('TIT2')}
ARTIST : {meta.get('TPE1')}
LENGTH : {length}
ALBUM  : {meta.get('TALB')}
TRACK  : {meta.get('TRCK')}
===============================
""".strip()
    print(metadata, flush=True)


def exec(command: Cmd, pos: int, *args: Path | str):
    if Config._script_proc is not None:
        Config._script_proc.kill()
    cmd = [
        sys.executable, "_music_script.py",
        f"{command.value}", f"{pos}", *args
        ]
    p = Popen(cmd, stdout=PIPE)
    Config._script_proc = p
