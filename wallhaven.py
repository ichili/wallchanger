from bs4 import BeautifulSoup
import requests
import logging


class Wallhaven(object):
    """docstring for Wallhaven"""

    def __init__(self, arg=''):
        super(Wallhaven, self).__init__()
        self.arg = arg
        self.logger = logging.getLogger('glogger')

    def _get_page(self, url):
        try:
            response = requests.get(url)
        except:
            self.logger.error('Error during loading page: ' + url)
            return ''
        return response.content

    def _get_image_url(self, url):
        page = self._get_page(url)
        soup = BeautifulSoup(page, "html.parser")
        wp = soup.find("img", {"id": "wallpaper"})['src']
        url = "https:" + wp
        return url

    def _get_urls(self, pages):
        urls = []
        for page in pages:
            urls.append(self._get_image_url(page))
        return urls

    def get_random(self, count=24):
        url = "https://alpha.wallhaven.cc/random"
        page = self._get_page(url)
        soup = BeautifulSoup(page, "html.parser")
        pages = [item['href'] for item in soup.findAll("a", {"class": "preview"})][:count]
        return self._get_urls(pages)
