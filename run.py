import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
print(results.prettify())


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
        return True


while True:
    print("Welcome to . \n")
    number = input("Enter bla bla: \n")
    choice = Choice(number)
    if choice.validate_choice():
        print("Valid")
        break
