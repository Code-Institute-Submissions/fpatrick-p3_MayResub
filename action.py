import scraper
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class User:

    api = 'HzKEwEi5j%z$fgAjtuK8S'
    sender = 'wescraper.message@outlook.com'

    def __init__(self):
        self.url = ""
        self.title = ""
        self.desired_price = 00.00
        self.price = ""
        self.availability = ""
        self.email = ""
        self.html = ""

    def send_email(self):
        convert = MIMEText(self.html, 'html')
        message = MIMEMultipart("alternative")
        message.attach(convert)
        message['Subject'] = f'Wescraper: "{self.title}" price dropped! '
        message['From'] = self.from_email
        message['To'] = self.email
        try:
            server = smtplib.SMTP('smtp.office365.com', 587)
            server.ehlo()
            server.starttls()
            server.login(self.sender, self.api)
            server.sendmail(self.sender, self.email, message.as_string())
            server.quit()
        except:
            print(" ************ SMTP server connection error ************ ")

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


class Validate(scraper.Scrapping):
    """
    Get menu choice from user and validate
    :param option: The menu choice, can be a number 1-6
    """
    def __init__(self):
        scraper.Scrapping.__init__(self)
        self.choice = 99
        self.url = ""
        self.desired_price = 00.00
        self.email = ""
        self.price = 00.00

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
                self.desired_price = float(input("Please enter desired price: \n"))
                return False
            except ValueError as e:
                print(f"Invalid data! Please enter only numbers and try again. \n")

    def ask_email(self):
        while True:
            try:
                self.email = input("Please enter your email to receive alert on price drop: \n")
                return False
            except ValueError as e:
                print(f"Invalid data! Please enter only numbers and try again. \n")

    def ask_page(self):
        if self.url == '':
            self.url = input("Please enter the URL: \n")
        try:
            return self.make_soup(self.url)
        except:
            print(f"URL Couldn't be reached! Please verify and try again. \n")
            return False

    def check_price(self, price):
        price = price.replace('€', '')
        price = price.replace('£', '')
        self.price = float(price)
        print(f"ese eh o pricce arrumado {price}")

        if self.price <= self.desired_price:
            return True
        else:
            return False




