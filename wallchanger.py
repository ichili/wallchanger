import schedule
import time
import threading
import os.path
import config_manager
from log import setup_global_logger
from wallhaven import Wallhaven
from downloader import Downloader
from wallset import Changer


class Manager(object):
    def __init__(self, settings):
        self.changer = Changer()
        self.downloader = Downloader()
        self.settings = settings
        self._setup_schedule()

    def _setup_schedule(self):
        def run_threaded(job_func):
            job_thread = threading.Thread(target=job_func, daemon=True)
            job_thread.start()

        change_interval = self.settings['changeInterval']
        download_interval = self.settings['downloadInterval']
        self._next = schedule.every(change_interval).seconds.do(run_threaded, self.change)
        self._download_more = schedule.every(download_interval).seconds.do(run_threaded, self.download)

    def download(self):
        client = Wallhaven()
        urls = client.get_random(count=self.settings['count'])
        for url in urls:
            filename = url.split('/')[-1]
            file = os.path.join(self.settings['path'], filename)
            self.downloader.download(url, file)

    def change(self):
        self.changer.next(self.settings['path'])

    def download_more(self):
        self._download_more.run()

    def next(self):
        self._next.run()

    def delete(self):
        self.changer.delete()
        self.next()

    def run_pending(self):
        schedule.run_pending()

    def run_all(self):
        schedule.run_all()


def setup_logger():
    setup_global_logger()


def console_run():
    manager = setup_manager()
    manager.run_all()
    while 1:
        manager.run_pending()
        minInterval = min(manager.settings['changeInterval'], manager.settings['downloadInterval'])
        time.sleep(minInterval // 3)


def setup_manager():
    setup_logger()
    config = config_manager.read_config()
    return Manager(config)


if __name__ == '__main__':
    console_run()
