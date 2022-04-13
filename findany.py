import scrapping


class Keyword(scrapping.Scrape):
    """

    """
    def __init__(self, **kwargs):
        Scrape.__init__(self, **kwargs)
        self.url = kwargs["url"]
        self.element = kwargs["element"]
        self.attr = kwargs["attribute"]
        self.name = kwargs["name"]

    def amazon(self):
        Scrape.request_page(self)
        Scrape.make_soup(self)

    def teste(self):
        self.name = "aqui ganhou outro nome"
        print(self.attr)
        print(self.url)
        print(self.name)