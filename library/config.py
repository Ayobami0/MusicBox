"""Global Configuration object."""


from pathlib import Path


class Config:
    __PRESET_DIRS: set[Path] = set()

    def __init__(self) -> None:
        default_path = Path('jingles')
        if default_path.exists():
            self.__PRESET_DIRS.add(default_path)

    def load(self):
        ...

    def save(self):
        ...

    def include_dir(self, *dirs: str) -> None:
        """Add a new directory to check for songs."""
        for dir in dirs:
            new_dir = Path(dir)
            if new_dir.exists():
                self.__PRESET_DIRS.add(new_dir)

    def exclude_dir(self, dir: str) -> None:
        """Remove a directory from the existing."""
        existing_dir = Path(dir)
        if existing_dir in self.__PRESET_DIRS:
            self.__PRESET_DIRS.remove(existing_dir)

    def list_dir(self) -> list[Path]:
        """List supported directory to search for songs."""
        return [dir for dir in self.__PRESET_DIRS]
