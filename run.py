import ecommerce
import findany


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
                    f"Please choose a number between 0 and 6! You provided {self.option}"
                )
        except ValueError as e:
            print(f"Invalid data: {e}, please try again. \n")
            return False
        self.option = int(self.option)
        return True


print("Welcome to Wescraper \n")
while True:
    print("Enter option: 1. Track e-commerces price. | 2. Test")
    choice = Choice(input("1-2: "))
    choice.validate_choice()

    if choice.option == 1:
        print("Enter option: 1. Amazon. | 2. Argos | 3. CEX")
        choice = Choice(input("1-2: "))
        choice.validate_choice()
        if choice.option == 1:
            product = ecommerce.Amazon("https://www.amazon.co.uk/Scholl-Mens-Activ-Work-Insoles/dp/B00R6AEAMQ?pd_rd_w"
                                       "=TTV8V&pf_rd_p=5e97ba20-ec2a-48fd-9f86-be9c3582eca4&pf_rd_r=4H7Y45C98GNPCV6TBENH"
                                       "&pd_rd_r=100e523d-dfb3-4fec-a2ac-445463d3fe0b&pd_rd_wg=QMWSu&pd_rd_i=B00R6AEAMQ"
                                       "&ref_=pd_bap_d_rp_1_i&th=1")
            print("Title:")
            print(product.title())
            print("Price:")
            print(product.price())
            print(product.availability())
            break
        elif choice.option == 2:
            product = ecommerce.Argos("https://www.argos.ie/static/Product/partNumber/2803748.htm")
            print(product.title())
            print(product.price())
            break
        elif choice.option == 3:
            product = ecommerce.Smiths("https://www.currys.ie/ieen/tv-and-home-entertainment/televisions/televisions/samsung-ue43au7100kxxu-43-smart-4k-ultra-hd-hdr-led-tv-10222296-pdt.html")
            print(product.title())
            print(f"They sell for: {product.price()}")
            break





