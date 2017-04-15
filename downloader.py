import urllib.request
import logging


def _prepare_opener():
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)


def download(url, location):
    logger = logging.getLogger('glogger')
    try:
        urllib.request.urlretrieve(url, location)
    except:
        logger.exception('Error during loading image: ' + url)


_prepare_opener()
