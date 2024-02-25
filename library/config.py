"""Global Configuration object."""


from pathlib import Path
from subprocess import Popen


class Config:
    __PRESET_DIRS: set[Path] = set()
    __DEFAULT_PATH = Path("jingles")
    _script_proc: Popen | None = None

    @classmethod
    def load(cls):
        default_path = cls.__DEFAULT_PATH
        if default_path.exists():
            cls.__PRESET_DIRS.add(default_path)

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
        return [dir for dir in cls.__PRESET_DIRS]
