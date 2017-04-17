import urllib.request
import logging
import os.path
from os import makedirs


class Downloader(object):
    def __init__(self):
        self._prepare_opener()

    def _prepare_opener(self):
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-Agent',
                              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)

    def download(self, url, location):
        logger = logging.getLogger('glogger')
        if not os.path.isdir(location):
            try:
                makedirs(location)
            except:
                logger.exception('Cannot create directory: ' + location)
                return
        try:
            urllib.request.urlretrieve(url, location)
        except:
            logger.exception('Error during loading image: ' + url)
