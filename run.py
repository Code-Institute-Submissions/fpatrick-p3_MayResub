import ecommerce
import findany
import action


print("Welcome to Wescraper \n")
while True:
    print("Enter option: 1. Track e-commerces price. | 2. Test")
    choice = action.Validate()
    choice.ask_choice()
    if choice.choice == 1:
        print("Enter option: 1. Amazon. | 2. Argos | 3. Currys")
        choice.ecommerce_choice()

        user = action.User()
        if choice.choice == 1:
            validate = action.Validate()
            validate.ask_price()
            print(f"Price: {validate.number}")
            user.amazon_price = validate.number
            user.amazon_url = input("Please enter the amazon URL product: \n")
            product = ecommerce.Amazon(user.amazon_url)
            print("Title:")
            print(product.title())
            print("Price:")
            print(product.price())
            print(product.availability())
            break
        elif choice.choice == 2:
            product = ecommerce.Argos("https://www.argos.ie/static/Product/partNumber/2803748.htm")
            print(product.title())
            print(product.price())
            break
        elif choice.choice == 3:
            product = ecommerce.Currys(
                "https://www.currys.ie/ieen/tv-and-home-entertainment/televisions/televisions/samsung-ue43au7100kxxu-43-smart-4k-ultra-hd-hdr-led-tv-10222296-pdt.html")
            print(product.title())
            print(f"They sell for: {product.price()}")
            break




