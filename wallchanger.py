import sys
import schedule
import time
import downloader
import wallset
import os.path
import log
import configparser
from wallhaven import Wallhaven


def read_config():
    config = configparser.ConfigParser()
    try:
        config.read_file(open('settings.cfg'))
    except:
        return None
    options = config['All']
    settings = {}
    settings['path'] = options['ImagesDirectory']
    settings['count'] = int(options['count'])
    return settings


def setup_logger():
    logpath = os.path.dirname(sys.argv[0])
    logpath = os.path.join(logpath, 'log.txt')
    logger = log.setup_custom_logger('glogger', logpath)
    return logger


def download(path, count):
    client = Wallhaven()
    urls = client.get_random(count=count)
    for url in urls:
        fname = url.split('/')[-1]
        file = os.path.join(path, fname)
        downloader.download(url, file)


def set_wallpaper(path):
    wallset.set_wallpaper(path)


def main():
    conf = read_config()
    if not conf:
        sys.exit(1)
    path = conf['path']
    count = conf['count']
    setup_logger()
    schedule.every(5).minutes.do(lambda: set_wallpaper(path))
    schedule.every(60).minutes.do(lambda: download(path, count))
    schedule.run_all()
    while 1:
        schedule.run_pending()
        time.sleep(5)


if __name__ == '__main__':
    main()
