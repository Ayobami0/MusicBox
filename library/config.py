"""Global Configuration object."""


from pathlib import Path
from subprocess import Popen


class Config:
    __PRESET_DIRS: set[Path] = set()
    __DEFAULT_PATH: Path = Path("jingles")

    _surfix_glob = ''
    _script_proc: Popen | None = None

    @classmethod
    def load(cls):
        default_path = cls.__DEFAULT_PATH
        if default_path.exists():
            cls.__PRESET_DIRS.add(default_path)
            cls.__PRESET_DIRS.add(Path("."))

    def save(self):
        ...

    @classmethod
    def include_dir(cls, *dirs: str) -> None:
        """Add a new directory to check for songs."""
        for dir in dirs:
            new_dir = Path(dir)
            if new_dir.exists():
                cls.__PRESET_DIRS.add(new_dir)

    @classmethod
    def exclude_dir(cls, dir: str) -> None:
        """Remove a directory from the existing."""
        existing_dir = Path(dir)
        if existing_dir in cls.__PRESET_DIRS:
            cls.__PRESET_DIRS.remove(existing_dir)

    @classmethod
    def list_dir(cls) -> list[Path]:
        """List supported directory to search for songs."""
        return list(cls.__PRESET_DIRS)

    @classmethod
    def list_songs(cls) -> list[Path]:
        """List all songs in preset dir."""
        songs = set()

        for d in cls.__PRESET_DIRS:
            songs.update(d.glob('*.mp3'))
        return [s for s in songs]

    @classmethod
    def clear_list(cls) -> None:
        """Clear all the existing preset directory"""
        cls.__PRESET_DIRS.clear()
