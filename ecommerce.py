import scraper


class Amazon(scraper.Scrapping):

    def __init__(self, url):
        scraper.Scrapping.__init__(self, url)
        self.soup = scraper.Scrapping.make_soup(self)

    def title(self):
        try:
            title = self.soup.find("span", attrs={"id": 'productTitle'}).string.strip()
        except AttributeError:
            title = "Error getting the title. Is the product available?"

        return title

    def price(self):

        try:
            price = self.soup.find("span", attrs={'class': 'a-offscreen'}).string.strip()

        except AttributeError:
            price = "Error getting the price. Is the product available?"

        return price

    def availability(self):
        try:
            availability = self.soup.find("div", attrs={"id": 'availability'})
            availability = availability.find("span").string.strip()

        except AttributeError:
            availability = ""

        return availability


class Argos(scraper.Scrapping):

    def __init__(self, url):
        scraper.Scrapping.__init__(self, url)
        self.soup = scraper.Scrapping.make_soup(self)

    def title(self):
        try:
            title = self.soup.find("div", attrs={"id": 'primaryproductinfo'})
            title = title.find("h1").string.strip()

        except AttributeError:
            title = ""

        return title

    def price(self):

        try:
            price = self.soup.find("span", attrs={'class': 'price'}).string.strip()

        except AttributeError:
            price = "Error getting the price. Is the product available?"

        return price


class HN(scraper.Scrapping):

    def __init__(self, url):
        scraper.Scrapping.__init__(self, url)
        self.soup = scraper.Scrapping.make_soup(self)

    def title(self):
        try:
            title = self.soup.find("div", attrs={"class": 'productNamecustm'}).string.strip()
        except AttributeError:
            title = ""

        return title

    def price(self):

        try:
            price = self.soup.find("span", attrs={'class': 'price'}).string.strip()

        except AttributeError:
            price = "Error getting the price. Is the product available?"

        return price

