import scraper


class Keyword(scraper.Scrapping):
    """

    """
    def __init__(self, **kwargs):
        scraper.Scrapping.__init__(self, **kwargs)
        self.url = kwargs["url"]
        self.element = kwargs["element"]
        self.attr = kwargs["attribute"]
        self.name = kwargs["name"]

    def amazon(self):
        scraper.Scrapping.request_page(self)
        scraper.Scrapping.make_soup(self)

    def teste(self):
        self.name = "aqui ganhou outro nome"
        print(self.attr)
        print(self.url)
        print(self.name)