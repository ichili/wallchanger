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
        directory = os.path.dirname(location)
        if not os.path.isdir(directory):
            try:
                makedirs(directory)
            except:
                logger.exception('Cannot create directory: ' + directory)
                return
        try:
            urllib.request.urlretrieve(url, location)
        except:
            logger.exception('Error during loading image: ' + url)
