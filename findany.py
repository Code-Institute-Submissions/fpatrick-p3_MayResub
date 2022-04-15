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
        tags = self.soup.find_all('a', text=lambda t: t and self.word in t.lower())

        for tag in tags:
            if tag['href'][0] == 'h':
                return tags
        return False

    def find_by(self, element):
        tags = self.soup.find_all(element, text=lambda t: t and self.word in t)
        last_tag = None
        for tag in tags:
            if last_tag != tag.text:
                print(f"\nFound: {tag.text}")
                last_tag = tag.text
