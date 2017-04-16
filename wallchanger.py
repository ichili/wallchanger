import sys
import schedule
import time
import downloader
import wallset
import os.path
import log
import config_manager
from wallhaven import Wallhaven


def download(path, count):
    client = Wallhaven()
    urls = client.get_random(count=count)
    for url in urls:
        filename = url.split('/')[-1]
        file = os.path.join(path, filename)
        downloader.download(url, file)


def set_wallpaper(path):
    wallset.set_wallpaper(path)


def setup_logger():
    log.setup_global_logger()


def main():
    config = config_manager.read_config()
    setup_logger()
    change_wallpaper = lambda: set_wallpaper(config['path'])
    download_new_wallpapers = lambda: download(config['path'], config['count'])
    change_interval = config['changeInterval']
    download_interval = config['downloadInterval']
    schedule.every(change_interval).seconds.do(change_wallpaper)
    schedule.every(download_interval).seconds.do(download_new_wallpapers)
    schedule.run_all()
    while 1:
        schedule.run_pending()
        time.sleep(5)


if __name__ == '__main__':
    main()
