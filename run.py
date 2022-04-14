import ecommerce
import findany
import action

print("Welcome to Wescraper \n")
# While True to easily restart script
while True:
    print("Enter option: 1. Track e-commerces price. | 2. Advanced mode (keyword search)")
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
            user.amazon_price = validate.desired_price
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
            user.argos_price = validate.desired_price
            page = validate.ask_page()
            if page:
                product = ecommerce.Argos(page)
                print(product.title())
                print(product.price())
                break
        elif validate.choice == 3:
            validate.ask_price()
            user.currys_price = validate.desired_price
            page = validate.ask_page()
            if page:
                product = ecommerce.Currys(page)
                print(product.title())
                print(product.price())
                break

    if validate.choice == 2:
        valor = "€53.98"
        validate.ask_price()
        if validate.check_price(valor):
            print("Price dropped")
            break

        break


