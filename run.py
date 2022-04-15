import ecommerce
import findany
import action
import time
import pickle


def run_ecommerce(validate, class_name, av='n'):
    validate.ask_price()
    validate.ask_email()

    while True:
        # Ask url and return soup, receive false if except
        page = validate.ask_page()
        # If not except
        if page:
            if class_name == 'amazon':
                product = ecommerce.Amazon(page)
            elif class_name == 'argos':
                product = ecommerce.Argos(page)
            elif class_name == 'currys':
                product = ecommerce.Currys(page)
            # Instance user class to store data and be able to retrieve later
            user = action.User()
            user.url = validate.url
            user.title = product.title()
            user.desired_price = validate.desired_price
            user.email = validate.email
            if av == 'y':
                user.availability = product.availability()
            low_price = validate.compare_price(product.price())
            user.price = validate.price
            if low_price:
                print(f"\nFound: {user.title} for €{user.price}")
                user.alert_price()
                print("Price match successful. Email sent. Exiting application...")
                exit()
            else:
                print(f"\nFound: {user.title} for €{user.price}")
                print("Querying again in 10 minutes. Stop terminal to stop running (Ctrl + C on linux).")
                time.sleep(48)
        else:
            print("\nError fetching the URL.")
            break

print("Welcome to Wescraper \n")
# While True to easily restart script
while True:
    print("\nEnter option: 1. Track e-commerces price. | 2. Advanced mode (keyword search) | 3. Repeat last query "
          "| 0. Exit")
    # Instance validations class
    validate = action.Validate()
    # Ask to pick a number, param limit number os choices
    validate.ask_choice(2)
    if validate.choice == 1:
        print("\nEnter option: 1. Amazon. | 2. Argos | 3. Currys | 0. Restart Script")
        validate.ask_choice(3)
        if validate.choice == 1:
            # Ask and validate a price
            run_ecommerce(validate, 'Amazon', 'y')
        elif validate.choice == 2:
            run_ecommerce(validate, 'argos')
        elif validate.choice == 3:
            run_ecommerce(validate, 'currys')

    if validate.choice == 2:
        print("\nEnter option: 1. Search keyword by href. | 2. Search keyword by custom html element. "
              "| 0. Restart Script")
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

        elif validate.choice == 0:
            continue

    if validate.choice == 9:
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

    if validate.choice == 0:
        break
