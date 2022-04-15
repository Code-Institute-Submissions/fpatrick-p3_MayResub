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

    def find(self):
        results = self.soup.find_all('a', text=lambda t: t and self.word in t)
        last_tag = None
        for tag in results:
            if last_tag != tag.text:
                print(tag)
                print(tag.text)
                print(tag['href'])
                last_tag = tag.text

    def find_by(self, element):
        results = self.soup.find_all(element, text=lambda t: t and self.word in t)
        last_tag = None
        for tag in results:
            if last_tag != tag.text:
                print(tag)
                print(tag.text)
                print(tag['href'])
                last_tag = tag.text
