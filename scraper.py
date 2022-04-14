import requests
from bs4 import BeautifulSoup


class Scrapping:
    """
    Scrap a page looking for an id or class
    """

    def __init__(self):
        """
        Init class
        """
        self.url = ""

    def request_page(self):
        headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0) Gecko/20100101 Firefox/99.0"
        }

        return requests.get(self.url, headers=headers)

        # with open('test.html', 'w') as f:
        #    f.write(self.page.text)
        #    f.close()

    def make_soup(self, url):
        self.url = url
        page = self.request_page()
        return BeautifulSoup(page.content, "lxml")
