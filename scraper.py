import requests
from bs4 import BeautifulSoup


class Scrapping:
    """
    Scrap a page looking for an id or class
    """

    def __init__(self, url):
        """
        Init class
        :param url: what page will be scrapped
        :param ident: html id that is needed  to be found
        :param cla: html class that is needed  to be found
        """
        self.url = url

    def request_page(self):
        headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0) Gecko/20100101 Firefox/99.0"
        }
        r = requests.get(self.url, headers=headers)

        with open('test.html', 'w') as f:
            f.write(r.text)
            f.close()
        return r

    def make_soup(self):
        page = self.request_page()
        return BeautifulSoup(page.content, "lxml")