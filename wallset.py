import ctypes
import random
import os.path
import logging
from os import walk


def _set_wallpaper(path):
    try:
        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 3)
    except:
        logger.exception('Error appeared while setting desktop wallpaper')


def choose_wallpaper(path):
    files = []
    try:
        for (dp, dn, fn) in walk(path):
            files.extend(fn)
    except OSError:
        logger.exception('Error on acessing images directory')
    return random.choice(files)


def set_wallpaper(path):
    file = choose_wallpaper(path)
    file = os.path.join(path, file)
    _set_wallpaper(file)


logger = logging.getLogger('glogger')