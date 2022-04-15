import ecommerce
import findany
import action
import time
import pickle

print("Welcome to Wescraper \n")
# While True to easily restart script
while True:
    print("\nEnter option: 1. Track e-commerces price. | 2. Advanced mode (keyword search) | 0. Exit")
    # Instance validations class
    validate = action.Validate()
    # Ask to pick a number, param limit number os choices
    validate.ask_choice(2)
    if validate.choice == 1:
        print("\nEnter option: 1. Amazon. | 2. Argos | 3. Currys | 0. Restart Script")
        validate.ask_choice(3)
        if validate.choice == 1:
            # Ask and validate a price
            validate.ask_price()
            validate.ask_email()

            while True:
                # Ask url and return soup, receive false if except
                page = validate.ask_page()
                # If not except
                if page:
                    product = ecommerce.Amazon(page)
                    # Instance user class to store data and be able to retrieve later
                    user = action.User()
                    user.url = validate.url
                    user.title = product.title()
                    user.desired_price = validate.desired_price
                    user.email = validate.email
                    user.availability = product.availability()
                    low_price = validate.check_price(product.price())
                    user.price = validate.price
                    if low_price:
                        print("Low price, good")
                        exit()
                    else:
                        print("High price")
                        print(f"title: {user.title}")
                        print(f"price: {user.price}")
                        print(f"desired: {user.desired_price}")
                        print(f"email: {user.email}")

                        time.sleep(48)
                else:
                    break

        elif validate.choice == 2:
            validate.ask_price()
            user.desired_price = validate.desired_price
            page = validate.ask_page()
            if page:
                product = ecommerce.Argos(page)
                print(product.title())
                print(product.price())
                break
        elif validate.choice == 3:
            validate.ask_price()
            user.desired_price = validate.desired_price
            page = validate.ask_page()
            if page:
                product = ecommerce.Currys(page)
                print(product.title())
                print(product.price())
                break
        elif validate.choice == 0:
            continue

    if validate.choice == 2:
        print("\nEnter option: 1. Search keyword by href. | 2. Search keyword by custom html element. | 9. Repeat last keyword search | 0. Restart Script")
        validate.ask_choice(2)
        if validate.choice == 1:
            page = validate.ask_page()
            if page:
                user = action.User()
                user.keyword = input("Please enter a keyword:\n")
                user.url = validate.url

                with open('last_query.obj', 'wb') as file:
                    pickle.dump(user, file)

                query = findany.Keyword(page, user.keyword)
                query.find()
        elif validate.choice == 2:
            keyword = "key"
        elif validate.choice == 9:
            try:
                with open('last_query.obj', 'rb') as file:
                    user = pickle.load(file)
            except:
                print("Deu ruim abrindo o arquivo la")
                pass
            validate.url = user.url
            page = validate.ask_page()
            if page:
                query = findany.Keyword(page, user.keyword)
                query.find()
        elif validate.choice == 0:
            continue

    if validate.choice == 0:
        break
