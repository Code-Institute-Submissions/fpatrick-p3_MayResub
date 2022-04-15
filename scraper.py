import requests
from bs4 import BeautifulSoup


class Scrapping:
    """
    Get html from pages and make_soup to manipulate data
    """
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0) Gecko/20100101 Firefox/99.0"
    }

    def __init__(self):
        """
        Init class
        """

    def request_page(self, url):

        return requests.get(url, headers=self.headers)

    def make_soup(self, url):
        page = self.request_page(url)
        return BeautifulSoup(page.text, "lxml")
