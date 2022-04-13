import scraper


class Amazon(scraper.Scrapping):

    def __init__(self, url):
        scraper.Scrapping.__init__(self, url)
        self.soup = scraper.Scrapping.make_soup(self)

    def get_title(self):
        try:
            # Outer Tag Object
            title = self.soup.find("span", attrs={"id": 'productTitle'})

            # Inner NavigableString Object
            title_value = title.string

            # Title as a string value
            title_string = title_value.strip()

            # # Printing types of values for efficient understanding
            # print(type(title))
            # print(type(title_value))
            # print(type(title_string))
            # print()

        except AttributeError:
            title_string = ""

        return title_string

    def get_price(self):

        try:
            price = self.soup.find("span", attrs={'class': 'a-offscreen'}).string.strip()

        except AttributeError:
            price = "Error getting the price. Is the product available?"

        return price

    def get_availability(self):
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

    def get_title(self):
        try:
            title = self.soup.find("div", attrs={"id": 'primaryproductinfo'})
            title = title.find("h1").string.strip()

        except AttributeError:
            title = ""

        return title

    def get_price(self):

        try:
            price = self.soup.find("span", attrs={'class': 'price'}).string.strip()

        except AttributeError:
            price = "Error getting the price. Is the product available?"

        return price