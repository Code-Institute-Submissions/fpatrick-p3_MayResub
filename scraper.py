import requests
from bs4 import BeautifulSoup


class Scrapping:
    """
    Scrap a page looking for an id or class
    """
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0) Gecko/20100101 Firefox/99.0"
    }

    def __init__(self):
        """
        Init class
        """

    def request_page(self, url):

        r = requests.get(url, headers=self.headers)

        with open('test.html', 'w') as f:
            f.write(r.text)
            f.close()

        return r

    def make_soup(self, url):
        page = self.request_page(url)
        return BeautifulSoup(page.text, "lxml")
