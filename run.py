import requests
from bs4 import BeautifulSoup


class Choice:
    """
    Get menu choice from user and validate
    :param option: The menu choice, can be a number 1-6
    """

    def __init__(self, option):
        self.choice = option

    def validate_choice(self):
        """
        Convert choice to int, raise exception if wrong option or can't be converted
        :return: True if passes, False if except
        """
        try:
            if int(self.choice) > 6:
                raise ValueError(
                    f"Please choose a number between 0 and 6, you provided {self.choice}"
                )
        except ValueError as e:
            print(f"Invalid data: {e}, please try again. \n")
            return False
        self.choice = int(self.choice)
        return True


class Scrap:
    """
    Scrap a page looking for an id or class
    """

    def __init__(self, url, ident="", cla=""):
        """
        Init class
        :param url: what page will be scrapped
        :param ident: html id that is needed  to be found
        :param cla: html class that is needed  to be found
        """
        self.url = url
        self.id_html = ident
        self.class_html = cla
        self.element = ""

    def request_page(self):
        return requests.get(self.url)

    def make_soup(self):
        page = self.request_page()
        mix_soup = BeautifulSoup(page.content, "html.parser")
        return mix_soup.find(id=self.id_html)


print("Welcome to . \n")
while True:
    choice = Choice(input("Enter bla bla: \n"))
    if choice.validate_choice():
        print(choice.choice)
        print("Valid")

    if choice.choice == 1:
        scrap = Scrap("https://realpython.github.io/fake-jobs/", "ResultsContainer")
        result = scrap.make_soup()
        print(result.prettify())
        break
    else:
        print("foi pro else")
        break
