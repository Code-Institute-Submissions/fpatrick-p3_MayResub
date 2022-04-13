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
                    f"Please choose a number between 0 and 6, you provided {self.option}"
                )
        except ValueError as e:
            print(f"Invalid data: {e}, please try again. \n")
            return False
        self.option = int(self.option)
        return True


print("Welcome to . \n")
while True:
    choice = Choice(input("Enter bla bla: \n"))
    if choice.validate_choice():
        print(choice.option)
        print("Valid")

    if choice.option == 1:
        product = ecommerce.Amazon("https://www.amazon.co.uk/QNAP-TS-251-2GB-Network-attached-multimedia/dp/B015CDDPD8/?_encoding"
                        "=UTF8&pd_rd_w=kzHMt&pf_rd_p=d49a09ba-36cd-426a-aae5-561eb64671fb&pf_rd_r=7CE001PPXRCVD79VG0YE"
                        "&pd_rd_r=69968122-3dc7-4a74-9911-351a2ae1dc61&pd_rd_wg=WNEln&ref_"
                        "=pd_gw_pd_aw_di_ci_int_sci_gw_atf_m_1")
        print("Title:")
        print(product.get_title())
        print("Price:")
        print(product.get_price())

        break
    elif choice.option == 2:
        teste = ecommerce.Argos("https://www.argos.ie/static/Product/partNumber/2803748.htm")
        print(teste.get_title())
        print(teste.get_price())
        break
