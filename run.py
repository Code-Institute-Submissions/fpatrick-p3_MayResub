import ecommerce
import findany
import action
import scraper

print("Welcome to Wescraper \n")
while True:
    print("Enter option: 1. Track e-commerces price. | 2. Test")
    choice = action.Validate()
    choice.ask_choice(2)
    if choice.choice == 1:
        print("Enter option: 1. Amazon. | 2. Argos | 3. Currys")
        choice.ask_choice(3)

        user = action.User()
        if choice.choice == 1:
            validate = action.Validate()
            validate.ask_price()
            print(f"Price: {validate.number}")
            user.amazon_price = validate.number


            user.amazon_url = input("Please enter the amazon URL product: \n")
            scrap = scraper.Scrapping(user.amazon_url)

            product = ecommerce.Amazon(scrap.make_soup())
            print("Title:")
            print(product.title())
            print("Price:")
            print(product.price())
            print(product.availability())
            break
        elif choice.choice == 2:
            scrap = scraper.Scrapping("https://www.argos.ie/static/Product/partNumber/2803748.htm")
            product = ecommerce.Argos(scrap.make_soup())
            print(product.title())
            print(product.price())
            break
        elif choice.choice == 3:
            scrap = scraper.Scrapping("https://www.currys.ie/ieen/tv-and-home-entertainment/televisions/televisions/samsung-ue43au7100kxxu-43-smart-4k-ultra-hd-hdr-led-tv-10222296-pdt.html")
            product = ecommerce.Currys(scrap.make_soup())
            print(product.title())
            print(f"They sell for: {product.price()}")
            break




