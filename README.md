# Wescraper

Wescraper is an awesome script that scrapes websites to track prices or keywords. 

**Please** read sections:
  - _Features and Use Cases_
  - _Instructions to run_
  - _Limitations_

Live link: https://wescraper.herokuapp.com/

![Screenshot 2022-04-15 at 20 41 28](https://user-images.githubusercontent.com/39106404/163626252-595bfd44-66e4-4e28-893a-c22534f664ee.png)
## Features and Use Cases

### Feature 1: Find keywords in discount websites

- __Use case: I want to buy an Apple Watch__
    </br></br>
  - Inside Wescraper select option 2 to enter keyword search, then option 1, enter apple watch, your email and the hotukdeals url (or other deals website)
    </br></br>
    ![Screenshot 2022-04-15 at 21 21 41](https://user-images.githubusercontent.com/39106404/163628570-240c84a1-3c11-4940-8fe3-2eb70445842f.png)
    </br></br>
  - Leave the script open (or use CaS, see Instructions section). Every 15 minutes Wescraper will look again the website, to check if someone posted a apple watch deal
    </br></br>
    ![Screenshot 2022-04-15 at 21 23 46](https://user-images.githubusercontent.com/39106404/163628660-22781f63-ebb7-48d3-8b55-0b980d2b1624.png)
   </br></br>
  - Someone posted the deal I was waiting for
   </br></br>
    ![Screenshot 2022-04-15 at 20 49 29](https://user-images.githubusercontent.com/39106404/163628996-5dcb61ae-da33-4577-a48f-22ff2be2ce6e.png)
  </br></br>
  - Wescraper found it and sent an alert to my email
  </br></br>
    ![Screenshot 2022-04-15 at 21 28 10](https://user-images.githubusercontent.com/39106404/163629106-2817cf64-cfb6-445a-8aa4-3fedb2844c9e.png)
  </br></br>
  - And I got it in my email. Now I can open the url to see the deal and buy it.
  </br></br>
    <img src="https://user-images.githubusercontent.com/39106404/163627285-1ff40abf-b14a-4896-bb56-a7ca401b002d.jpeg" width="300">
  </br></br></br>
### Feature 2: Track price in big e-commerces websites
- __Use Case: I want to buy a new specific TV in amazon uk, currys.ie or argos.ie__
    </br></br>
  - Select option 1 Track price
    - enter a e-commerce option (1 to 3)
      - enter desired price (how much I want to pay)
        - enter email
          - enter product URL (copy and paste from browser)
            </br></br>
            ![Screenshot 2022-04-15 at 21 45 55](https://user-images.githubusercontent.com/39106404/163630610-922394b3-463e-4b0d-93bb-b647f9217693.png)
            </br></br>
  - Every 15 minutes Wescraper will verify if the product price is equal or lower than the price I want to pay and send a email when found
  </br></br>
    <img src="https://user-images.githubusercontent.com/39106404/163627348-7a0feb83-4fcd-4955-9cc7-01a2b6a8eb35.jpeg" width="300">
  </br></br>
  - Now I can just click the link and buy it.

### Feature 3: Repeat last query
- __Use Case: I closed Wescraper and want to resume where I left__
  - Enter option 3, and it will start tracking price or looking for keyword
  

## Instructions to run

### Simplest - _Run web mock terminal_
  Enter https://wescraper.herokuapp.com/
### Terminal Linux - _Run directly_
  * > clone wescraper
  * >cd to folder
  * >python3 run.py
    
### **_Recommended way_**: CaS - Command and Script (Linux, Advanced users)
* I developed a script called **CaS** https://github.com/fpatrick/cas
* It runs python3 scripts and bash commands in background using screen
* Use **CaS** to run **Wescraper** in background for as long as needed

## Limitations

* Websites can block Wescraper, especially if many query comes from same IP within a small-time frame
* Websites can block bots like Wescraper
* The SMTP server can only send a limited number of emails daily (around 100)

## Testing 

### Validator Testing 

- PEP8
  - No errors were returned from PEP8online.com


### Unfixed Bugs

Bugs not found.

## Deployment

- This project was deployed using Code Institute's mock terminal for Heroku.

- Steps for deployment: 
  - Fork or clone this repository
  - Create a new Heroku app
  - Set the build packs to Python and NodeJS in that order
  - Link the Heroku app to the repository
  - Click on Deploy
  

## Credits 

- https://medium.com/@neonforge/how-to-send-emails-with-attachments-with-python-by-using-microsoft-outlook-or-office365-smtp-b20405c9e63a
- https://www.journaldev.com/44473/scrape-amazon-product-information-beautiful-soup
- Code Institute for the deployment terminal