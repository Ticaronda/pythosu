from zipfile import ZipFile
import os

from pygame.sysfont import OpenType_extensions

def open_osz(file: str) -> None:
    """
    Extracts the contents of a .osz file into the maps directory.
    """
    with ZipFile(file, 'r') as zf:
        zf.printdir()
        filename: str = file.removesuffix(".osz")
        zf.extractall("maps/" + filename)

def open_osu(osu) -> None:
    """
    """
    with open(osu, 'r') as f:
        print(f.readlines())

if __name__ == "__main__":
    # open_osz("Reol - No title.osz")
    open_osu("maps/Reol - No title/Reol - No title (VINXIS) [toybot's Insane].osu")
