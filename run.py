import ecommerce
import findany
import action
import time
import pickle


def run_ecommerce(validate, user, first='yes', av='n'):
    if first == 'yes':
        validate.ask_price()
        user.desired_price = validate.desired_price
        validate.ask_email()
        user.email = validate.email
    else:
        validate.desired_price = user.desired_price
        validate.url = user.url

    while True:
        # Ask url and return soup, receive false if except
        page = validate.ask_page()
        # If not except
        if page:
            if user.class_name == 'amazon':
                product = ecommerce.Amazon(page)
            elif user.class_name == 'argos':
                product = ecommerce.Argos(page)
            elif user.class_name == 'currys':
                product = ecommerce.Currys(page)
            # Instance user class to store data and be able to retrieve later
            user.url = validate.url
            user.title = product.title()
            if av == 'yes':
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
                if user.alert_price():
                    print("Price match successful. Email sent. Exiting application...")
                else:
                    print("Email couldn't be sent")
                exit()
            else:
                print(f"\nFound: {user.title} for €{user.price}")
                print("Querying again in 10 minutes. Stop terminal to stop running (Ctrl + C on linux).")
                time.sleep(48)
        else:
            break


def run_query(validate, user, first='yes'):
    if first == 'yes':
        user.keyword = input("Please enter a keyword:\n").lower()
        validate.ask_email()
        user.email = validate.email
    else:
        validate.url = user.url
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
            user.class_name = 'amazon'
            run_ecommerce(validate, user, 'yes', 'yes')
        elif validate.choice == 2:
            user = action.User()
            user.class_name = 'argos'
            run_ecommerce(validate, user)
        elif validate.choice == 3:
            user = action.User()
            user.class_name = 'currys'
            run_ecommerce(validate, user)
        elif validate.choice == 0:
            continue

    if validate.choice == 2:
        print("\nEnter option: 1. Search keyword by href. | 0. Restart Script")
        print("* FYI: Select option 1 to query websites like hotukdeals.")
        validate.ask_choice(1)
        if validate.choice == 1:
            user = action.User()
            user.class_name = "keyword"
            run_query(validate, user)

        elif validate.choice == 0:
            continue

    if validate.choice == 3:
        try:
            with open('last_query.obj', 'rb') as file:
                user = pickle.load(file)
        except:
            print("\nError trying to retrieve last query!")


        if user.class_name == "amazon":
            run_ecommerce(validate, user, 'y', 'repeat')
        elif user.class_name == "argos":
            run_ecommerce(validate, user, 'repeat')
        elif user.class_name == "currys":
            run_ecommerce(validate, user, 'repeat')
        elif user.class_name == "keyword":
            run_query(validate, user, 'repeat')
        else:
            print("\nError running last query.")
            continue

    if validate.choice == 0:
        break
