import ecommerce
import findany
import action
import time
import pickle


def run_ecommerce(validate, user, class_name, av='n'):
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
            user.url = validate.url
            user.title = product.title()
            user.desired_price = validate.desired_price
            user.email = validate.email
            if av == 'y':
                user.availability = product.availability()
            low_price = validate.compare_price(product.price())
            user.price = validate.price
            try:
                with open('last_query.obj', 'wb') as file:
                    pickle.dump(user, file)
            except:
                print("Warning: Error saving data to repeat query later. Script will continue normally")
                pass
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
            break


def run_query(validate, user):
    user.keyword = input("Please enter a keyword:\n").lower()
    validate.ask_email()
    user.email = validate.email
    while True:
        page = validate.ask_page()
        if page:
            user.url = validate.url
            try:
                with open('last_query.obj', 'wb') as file:
                    pickle.dump(user, file)
            except:
                print("Warning: Error saving data to repeat query later. Script will continue normally")
                pass
            query = findany.Keyword(page, user.keyword)
            tags = query.find()
            last_tag = None
            if tags:
                for tag in tags:
                    if last_tag != tag.text:
                        if tag['href'][0] == 'h':
                            print(f"\nFound: {tag.text}")
                            print(f"Url: {tag['href']}")
                            last_tag = tag.text
                if user.alert_keyword(tags):
                    print("Keyword match successful. Email sent. Exiting application...")
                else:
                    print("Keyword match successful. But couldn't send email. Exiting application...")
                exit()
            else:
                print("\nResults not found.")
                print("Querying again in 10 minutes. To Stop running, stop terminal (Ctrl + C on linux).")
                time.sleep(48)
        else:
            break

print("Welcome to Wescraper \n")
# While True to easily restart script
while True:
    print("\nEnter option: 1. Track e-commerces price. | 2. Advanced mode (keyword search) | 3. Repeat last query "
          "| 0. Exit")
    # Instance validations class
    validate = action.Validate()
    # Ask to pick a number, param limit number os choices
    validate.ask_choice(3)
    if validate.choice == 1:
        print("\nEnter option: 1. Amazon. | 2. Argos | 3. Currys | 0. Restart Script")
        validate.ask_choice(3)
        if validate.choice == 1:
            # Ask and validate a price
            user = action.User()
            run_ecommerce(validate, user, 'Amazon', 'y')
        elif validate.choice == 2:
            user = action.User()
            run_ecommerce(validate, user, 'argos')
        elif validate.choice == 3:
            user = action.User()
            run_ecommerce(validate, user, 'currys')
        elif validate.choice == 0:
            continue

    if validate.choice == 2:
        print("\nEnter option: 1. Search keyword by href. | 2. Search keyword by custom html element. "
              "| 0. Restart Script")
        validate.ask_choice(2)
        if validate.choice == 1:
            user = action.User()
            run_query(validate, user)

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
