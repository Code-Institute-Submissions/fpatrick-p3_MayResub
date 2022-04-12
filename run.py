import requests
from bs4 import BeautifulSoup
import numpy as np

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


class Scrap:
    """
    Scrap a page looking for an id or class
    """

    def __init__(self, url, ident, cla=""):
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
        headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0) Gecko/20100101 Firefox/99.0"
        }
        pega = requests.get(self.url,headers=headers)
        print(pega.text)
        return requests.get(self.url)

    def make_soup(self):
        page = self.request_page()
        mix_soup = BeautifulSoup(page.content, "html.parser")
        return mix_soup.find(id=self.id_html)


print("Welcome to . \n")
while True:
    choice = Choice(input("Enter bla bla: \n"))
    if choice.validate_choice():
        print(choice.option)
        print("Valid")

    if choice.option == 1:
        scrap = Scrap("https://www.amazon.co.uk/QNAP-TS-251-2GB-Network-attached-multimedia/dp/B015CDDPD8/?_encoding=UTF8&pd_rd_w=kzHMt&pf_rd_p=d49a09ba-36cd-426a-aae5-561eb64671fb&pf_rd_r=7CE001PPXRCVD79VG0YE&pd_rd_r=69968122-3dc7-4a74-9911-351a2ae1dc61&pd_rd_wg=WNEln&ref_=pd_gw_pd_aw_di_ci_int_sci_gw_atf_m_1", "Asellprice")
        result = scrap.make_soup()
        print(result)
        break
    else:
        print("foi pro else")
        break
