import scrapping


class Amazon(scrapping.Scrape):

    def __init__(self, url):
        scrapping.Scrape.__init__(self, url)
        self.soup = scrapping.Scrape.make_soup(self)

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
