import ecommerce
import findany
import action
import scraper

print("Welcome to Wescraper \n")
# While True to easily restart script
while True:
    print("Enter option: 1. Track e-commerces price. | 2. Test")
    # Instance validations class
    validate = action.Validate()
    # Ask to pick a number, param limit number os choices
    validate.ask_choice(2)
    if validate.choice == 1:
        print("Enter option: 1. Amazon. | 2. Argos | 3. Currys")
        validate.ask_choice(3)
        # Instance user class to store data and be able to retrieve later
        user = action.User()
        if validate.choice == 1:
            # Ask and validate a price
            validate.ask_price()
            # User object store price
            user.amazon_price = validate.price
            # Ask url and return soup, receive false if except
            page = validate.ask_page()
            # If not except
            if page:
                product = ecommerce.Amazon(page)
                print("Title:")
                print(product.title())
                print("Price:")
                print(product.price())
                print(product.availability())
                break
        elif validate.choice == 2:
            validate.ask_price()
            user.argos_price = validate.price
            page = validate.ask_page()
            if page:
                product = ecommerce.Argos(page)
                print(product.title())
                print(product.price())
                break
        elif validate.choice == 3:
            validate.ask_price()
            user.currys_price = validate.price
            page = validate.ask_page()
            if page:
                product = ecommerce.Currys(page)
                print(product.title())
                print(product.price())
                break

    if validate.choice == 2:
        user = action.User()
        user.url = "http://osite.com"
        user.email = "dopync@gmail.com"
        user.desired_price = 32
        user.price = 12
        user.title = "Casinha de cocozinho"

        user.alert_price()


