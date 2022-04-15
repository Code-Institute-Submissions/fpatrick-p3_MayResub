import scraper


class Keyword(scraper.Scrapping):
    """

    """
    def __init__(self, soup, word):
        scraper.Scrapping.__init__(self)
        self.word = word
        self.soup = soup

    def amazon(self):
        scraper.Scrapping.request_page(self)
        scraper.Scrapping.make_soup(self)

    def teste(self):
        tags = self.soup.find_all('a', text=lambda t: t and self.word in t)
        print(type(tags))
        print(tags)
