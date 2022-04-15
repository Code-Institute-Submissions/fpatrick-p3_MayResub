# Wescraper

Wescraper is an awesome script that scrapes websites to track prices or keywords. 

Please read sections:
  - Features and Use Cases
  - Instructions to use
  - Limitations

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
  - Leave the script open (or use CaS, scroll down to know more). Every 15 minutes Wescraper will look again the website, to check if someone posted a apple watch deal
    ![Screenshot 2022-04-15 at 21 23 46](https://user-images.githubusercontent.com/39106404/163628660-22781f63-ebb7-48d3-8b55-0b980d2b1624.png)
   </br></br>
  - Someone posted the deal you were waiting for
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
  - Select option 1 Track price, then enter desired website option, desired price and product URL (copy and paste from browser)
    </br></br>
    ![Screenshot 2022-04-15 at 21 45 55](https://user-images.githubusercontent.com/39106404/163630610-922394b3-463e-4b0d-93bb-b647f9217693.png)
    </br></br>
  - Each 15 minutes Wescraper will verify if the product price is equal or lower than the price I want to pay and send a email when found
  </br></br>
    <img src="https://user-images.githubusercontent.com/39106404/163627348-7a0feb83-4fcd-4955-9cc7-01a2b6a8eb35.jpeg" width="300">
  </br></br>
  - Now I can just click the link and buy it.

### Feature 3: Repeat last query
- __Use Case: I closed Wescraper and want to resume where I left__
  - Enter option 3, and it will start tracking price or looking for keyword






### Features Left to Implement

- The cards are made dynamically, many other tools or calculators can be added

## Testing 

### Validator Testing 

- PEP8
  - No errors were returned from PEP8online.com


### Unfixed Bugs

Bugs not found to date.

## Deployment

- This project was deployed using Code Institute's mock terminal for Heroku.

- Steps for deployment.: 
  - Fork or clone this repository
  - Create a new Heroku app
  - Set the build packs to Python and NodeJS in that order
  - Link the Heroku app to the repository
  - Click on Deploy
  

## Credits 

- Code Institute for the deployment terminal