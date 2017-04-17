import ctypes
import random
import os.path
import logging
from os import walk


class Changer(object):
    def __init__(self):
        self.logger = logging.getLogger('glogger')

    def _set_wallpaper(self, path):
        try:
            SPI_SETDESKWALLPAPER = 20
            ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 3)
        except:
            self.logger.exception('Error appeared while setting desktop wallpaper')
        else:
            self._current = path

    def choose_wallpaper(self, path):
        files = []
        try:
            for (dp, dn, fn) in walk(path):
                files.extend(fn)
        except OSError:
            self.logger.exception('Error on accessing images directory')
        return random.choice(files)

    def set_wallpaper(self, path):
        file = self.choose_wallpaper(path)
        file = os.path.join(path, file)
        self._set_wallpaper(file)

    def next(self, directory):
        self.set_wallpaper(directory)

    def delete(self):
        try:
            os.remove(self._current)
        except:
            self.logger.exception('Unable to remove file ' + self._current)
