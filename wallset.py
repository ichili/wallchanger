import ctypes
import random
import os.path
from os import walk


def _set_wallpaper(path):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 3)


def choose_wallpaper(path):
    files = []
    for (dp, dn, fn) in walk(path):
        files.extend(fn)
    return random.choice(files)


def set_wallpaper(path):
    file = choose_wallpaper(path)
    file = os.path.join(path, file)
    _set_wallpaper(file)
