import requests
from bs4 import BeautifulSoup


class Choice:
    """
    Get menu choice from user and validate
    :param option: The menu choice, can be a number 1-6
    """

    def __init__(self, option):
        self.option = option

    def validate_choice(self):
        """
        Convert choice to int, raise exception if wrong option or can't be converted
        :return: True if passes, False if except
        """
        try:
            if int(self.option) > 6:
                raise ValueError(
                    f"Please choose a number between 0 and 6, you provided {self.option}"
                )
        except ValueError as e:
            print(f"Invalid data: {e}, please try again. \n")
            return False
        self.option = int(self.option)
        return True


class Scrape:
    """
    Scrap a page looking for an id or class
    """

    def __init__(self, url):
        """
        Init class
        :param url: what page will be scrapped
        :param ident: html id that is needed  to be found
        :param cla: html class that is needed  to be found
        """
        self.url = url

    def request_page(self):
        headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0) Gecko/20100101 Firefox/99.0"
        }
        return requests.get(self.url, headers=headers)

    def make_soup(self):
        page = self.request_page()
        return BeautifulSoup(page.content, "lxml")


class Amazon(Scrape):

    def __init__(self, url):
        Scrape.__init__(self, url)
        self.soup = Scrape.make_soup(self)

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


class Keyword(Scrape):
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


print("Welcome to . \n")
while True:
    choice = Choice(input("Enter bla bla: \n"))
    if choice.validate_choice():
        print(choice.option)
        print("Valid")

    if choice.option == 1:
        product = Amazon("https://www.amazon.co.uk/QNAP-TS-251-2GB-Network-attached-multimedia/dp/B015CDDPD8/?_encoding"
                        "=UTF8&pd_rd_w=kzHMt&pf_rd_p=d49a09ba-36cd-426a-aae5-561eb64671fb&pf_rd_r=7CE001PPXRCVD79VG0YE"
                        "&pd_rd_r=69968122-3dc7-4a74-9911-351a2ae1dc61&pd_rd_wg=WNEln&ref_"
                        "=pd_gw_pd_aw_di_ci_int_sci_gw_atf_m_1")
        print(product.get_title())

        break
    elif choice.option == 2:
        teste = Ecommerce(url="Essa eh a url", element="nao pode falta o element", attribute="o atributo", name="o nome")
        teste.teste()
        break