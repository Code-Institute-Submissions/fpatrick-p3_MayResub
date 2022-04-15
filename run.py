import ecommerce
import findany
import action

# To run again in 10 minutes
import time
# For store objs
import pickle


def run_ecommerce(validate, user, first='yes', av='n'):
    """
    Call all classes and methods necessary to load ecommerce objects
    """
    # If first time running
    if first == 'yes':
        # Ask user for price
        validate.ask_price()
        # Store price in user object
        user.desired_price = validate.desired_price
        # Ask user for email
        validate.ask_email()
        # Store email in user object
        user.email = validate.email
    # It is repeating last query
    else:
        # Validate get user desired price so it can work properly
        validate.desired_price = user.desired_price
        # Validate get user url so it can work properly
        validate.url = user.url
    # Repeat if page exists. Needed to rerun block in 10 minutes time
    while True:
        # Ask url and return soup, return false if except
        page = validate.ask_page()
        # If not except
        if page:
            # What object will be created
            if user.class_name == 'amazon':
                product = ecommerce.Amazon(page)
            elif user.class_name == 'argos':
                product = ecommerce.Argos(page)
            elif user.class_name == 'currys':
                product = ecommerce.Currys(page)
            # Store url returned after asking page
            user.url = validate.url
            # Store product title
            user.title = product.title()
            # If availability field is there
            if av == 'yes':
                user.availability = product.availability()
            # Clean money symbol and compare desired price with actual price, true if price is lower than desired
            low_price = validate.compare_price(product.price())
            # Store price that was validated
            user.price = validate.price
            # Try to create a file with user object to reuse
            try:
                with open('last_query.obj', 'wb') as file:
                    pickle.dump(user, file)
            except:
                print("Warning: Error saving data to repeat query later. Script will continue normally")
                pass

            if low_price:
                print(f"\nFound: {user.title} for €{user.price}")
                # Send email with price alert, return true if it was successful
                if user.alert_price():
                    print("Price match successful. Email sent. Exiting application...")
                else:
                    print("Email couldn't be sent. Daily server limit reached? Exiting application...")
                exit()
            else:
                print(f"\nFound: {user.title} for €{user.price}")
                print("Querying again in 15 minutes. Stop terminal to stop running (Ctrl + C on linux).")
                # Wait in seconds to repeat the loop and query price again
                time.sleep(900)
        else:
            # If page fail to load, break the loop and restart script.
            break


def run_query(validate, user, first='yes'):
    """
    Call all classes and methods necessary to load keyword query objects
    Explanations same as run_ecommerce
    """
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
                    print("Keyword match successful. But couldn't send email. Daily server limit reached? Exiting application...")
                exit()
            else:
                print("\nResults not found.")
                print("Querying again in 15 minutes. To Stop running, stop terminal (Ctrl + C on linux).")
                time.sleep(900)
        else:
            break


print("********************************************************************")
print("*                  Welcome to Wescraper v1.0.0                     *")
print("*     Instructions and source: https://github.com/fpatrick/p3      *")
print("********************************************************************")
# Loop to easily restart script
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
            # Instance user class to store data and be able to retrieve later
            user = action.User()
            # Class name to be used and stored for reuse
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
            # Continue code and restart loop (script)
            continue

    if validate.choice == 2:
        print("\nEnter option: 1. Search keyword by href. | 0. Restart Script")
        print("*FYI: Select option 1 to query websites like hotukdeals.")
        validate.ask_choice(1)
        if validate.choice == 1:
            user = action.User()
            user.class_name = "keyword"
            run_query(validate, user)

        elif validate.choice == 0:
            continue

    if validate.choice == 3:
        # Try to load user obj stored
        try:
            with open('last_query.obj', 'rb') as file:
                user = pickle.load(file)
        except:
            print("\nError trying to retrieve last query!")
        # Run based on last used class
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
        # Stop loop and finish script
        break
