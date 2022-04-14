import scraper
import smtplib

import email
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Validate(scraper.Scrapping):
    """
    Get menu choice from user and validate
    :param option: The menu choice, can be a number 1-6
    """
    def __init__(self):
        scraper.Scrapping.__init__(self)
        self.choice = 99
        self.price = 99
        self.url = ""

    def ask_choice(self, limit):
        """
        Convert choice to int, raise exception if wrong option or can't be converted
        :return: True if passes, False if except
        """
        while True:
            try:
                self.choice = int(input(f"1-{limit}: "))
                if self.choice > limit:
                    raise ValueError(
                        f"Please choose a number between 0 and {limit}! You provided {self.choice}"
                    )
                return False
            except ValueError as e:
                print(f"Please choose a number between 0 and {limit}! You provided invalid data: {e}\n")

    def ask_price(self):
        while True:
            try:
                self.price = int(input("Please enter desired price: \n"))
                return False
            except ValueError as e:
                print(f"Invalid data! Please enter only numbers and try again. \n")

    def ask_page(self):
        self.url = input("Please enter the URL: \n")
        try:
            return self.make_soup(self.url)
        except:
            print(f"URL Couldn't be reached! Please verify and try again. \n")
            return False


class User:

    login = 'wescraper.message@outlook.com'
    password = 'HzKEwEi5j%z$fgAjtuK8S'
    from_email = 'wescraper.message@outlook.com'

    def __init__(self):
        self.url = ""
        self.title = ""
        self.desired_price = 0
        self.price = 0
        self.email = ""
        self.html = ""

    def send_email(self):
        convert = MIMEText(self.html, 'html')
        message = MIMEMultipart("alternative")
        message.attach(convert)
        message['Subject'] = f'Wescrape: "{self.title}" price dropped! '
        message['From'] = self.from_email
        message['To'] = self.email
        try:
            server = smtplib.SMTP('smtp.office365.com', 587)
            server.ehlo()
            server.starttls()
            server.login(self.login, self.password)
            server.sendmail(self.from_email, self.email, message.as_string())
            server.quit()
        except:
            print(" ************ SMPT server connection error ************ ")

    def alert_price(self):
        self.html = f"""
                    <html>
                      <body>
                        <h2> Good news! The price dropped. </h2>
                        <p><b></b>
                           You have been waiting to buy <b>{self.title}</b> for <b>€{self.desired_price}</b>.
                           <br>
                           <h3>The price right now is <b>€{self.price}</b></h3>
                           <br>
                           Time to run and buy it: <b>{self.url}</b>
                        </p>
                      </body>
                    </html>
                """
        self.send_email()

