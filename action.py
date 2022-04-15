import scraper
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class User:
    """
    Store all user input data for send email and rerun last query
    """
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
        self.keyword = ""
        self.class_name = ""

    def send_email(self, subject):
        convert = MIMEText(self.html, 'html')
        message = MIMEMultipart("alternative")
        message.attach(convert)
        message['Subject'] = subject
        message['From'] = self.sender
        message['To'] = self.email
        try:
            server = smtplib.SMTP('smtp.office365.com', 587)
            server.ehlo()
            server.starttls()
            server.login(self.sender, self.api)
            server.sendmail(self.sender, self.email, message.as_string())
            server.quit()
            return True
        except:
            print(" ************ SMTP server connection error ************ ")
            return False

    def alert_price(self):
        subject = f'Wescraper: "{self.title}" price dropped! '
        self.html = f"""
                    <html>
                      <body>
                        <h2> Good news! The price dropped. </h2>
                        <p><b></b>
                           You have been waiting to buy <b>{self.title}</b> for <b>€{self.desired_price}</b>.
                           <br>
                           <h3>The price right now is <b>€{self.price}. {self.availability}</b></h3>
                           <br>
                           Time to run and buy it: <b>{self.url}</b>
                        </p>
                      </body>
                    </html>
                """
        if self.send_email(subject):
            return True
        else:
            return False

    def alert_keyword(self, tags):
        subject = f'Wescraper: Keywords found for "{self.keyword}"'
        self.html = f"""
                    <html>
                      <body>
                        <h2> Good news! Keywords were found. </h2>
                        <p><b></b>
                           You asked Wescraper to look for <b>{self.keyword}</b> in <b>{self.url}</b>.
                           <br>
                           <h3>Those keywords were found:</b></h3>
                           <br>
                    """
        last_tag = None
        for tag in tags:
            if last_tag != tag.text:
                if tag['href'][0] == 'h':
                    self.html += f"<b>Title:</b> {tag.text}"
                    self.html += f"<b>Url:</b> {tag['href']}"
                    self.html += f"<br>"
                    last_tag = tag.text
        self.html += f"""                   
                        </p>
                      </body>
                    </html>
                """
        if self.send_email(subject):
            return True
        else:
            return False


class Validate(scraper.Scrapping):
    """
    Get inputs from user and validate it when necessary
    """
    def __init__(self):
        # Inherit scrapping to request and validate page
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
                self.choice = int(input(f"0-{limit}: "))
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
                self.desired_price = float(input("Please enter desired price (without symbols €) : \n"))
                return False
            except ValueError as e:
                print(f"Invalid data! Please enter only numbers and try again. \n")

    def ask_email(self):
        print("* FYI: First email will arrive at spam folder. Mark it as secure. * ")
        while True:
            try:
                self.email = input("Please enter your email CAREFULLY to receive alert on price drop: \n")
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

    def compare_price(self, price):
        price = price.replace('€', '')
        price = price.replace('£', '')
        try:
            self.price = float(price)
        except ValueError as e:
            print(f"\nError trying to convert price. The website may be blocking bot access.")
            exit()

        if self.price <= self.desired_price:
            return True
        else:
            return False




