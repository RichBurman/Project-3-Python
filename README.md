![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Pizza World 

<img src="assets/images/README/responsive.png" width="800" height="600" alt="Image of Am I responsive"> 


Pizza World is a Python terminal program which runs in the Code Institute mock terminal on Heroku. 


Pizza World is designed for a pizza company which currently sells 3 types of pizza:
- Cheese Pizza
- Ham Pizza 
- Sausage Pizza

Pizza World allows the user to perform various functions which are listed below: 

- Enter and store daily sales for the 3 types of pizza into Pizza World. 
- Order new stock of pizzas for the pizza company
- View current stock levels of the 3 types of pizza
- View a sales report which shows all the sales of pizza by Pizza World
- View a Profit Report which shows the user which displays all the profits from the sales data and diplay the total profit
- View the most profitable pizza which shows the user which pizza has made the most profits for Pizza World and shows how much this profit is



[Here is the live version of the project](https://pizza-world.herokuapp.com/)

[Here is a live link to the google worksheet](https://docs.google.com/spreadsheets/d/1S1hgp-PmgAoM8KUjN3stYeTxWITjOD4pQTnUQbdar2Y/edit?usp=sharing)

## Data Model
- Flowchart plan
    - I decided to use a Flowchart plan to model and map the functionality of Pizzaworld. 
    - I was able to clearly see the path I wanted to follow when designing and creating Pizzaworld. 
    - This allowed me to ensure all areas of PizzaWorld were positioned correctly and had a blueprint to follow in order to produce a fully functioning program. 
    - I wanted to create a means of storing all the data inputted and created from PizzaWorld into a google worksheet to enable the user to use this data to aid with future business decisions i.e which pizzas are popular, whether more stock is needed for a particular pizza on a daily basis, which pizzas are providing the business with the most profit.
    - It was vital that are data entered into Pizza World was checked for validation for being accepted into the worksheet and Pizza World. If any data was not valid, the user needed to be informed and offered the opportunity to enter valid data. 

    ### Flowchart Model


    <img src="assets/images/README/plan.png" width="500" height="400" alt="Image of Flowchart"> 

## How it works

### Menu

Pizza World welcomes users to it's menu. This allows users to 





- Future Features


## Testing

I have manually tested this project by undertaking the following steps:

- Passed the code through a PEP8 linter and confirmed there are no problems
- Given invalid inputs: strings when numbers are expected, more than 3 numbers
- Tested in my local terminal and the Code Institute Heroku terminal

Manual testing example below:

<img src="assets/images/README/validation_and_error_checks.png" width="500" height="250" alt="Image of manual testing validation and errors checks"> 


## Bugs
 ### Solved Bugs

- I was receiving an error index because I had forgotten to add 'int' at the start of the various (profit_row). I fixed this by adding 'int' to all of the profit_row variables, which allowed the calculation to take place.
<img src="assets/images/README/solved_bug.png" width="500" height="250" alt="Image of solved bug"> 


### Remaining Bugs

- No bugs remaining

## Validator Testing

- PEP8
    - No errors were returned from pep8ci.herokuapp.com expect for 'line too long' errors

<img src="assets/images/README/CI_python_linter.png">

## Deployment

- The project was deployed using Code Institute's mock terminal for Heroku.

    - Steps for deployment
        - Create a new Heroku app
        - Add Config Vars for CREDS and PORT
        - Set the buildbacks to Pythong and NodeJS in that order
        - Link the Heroku app to the repository
        - Click on Deploy

## Credits

- Code Institute for the deployment terminal 
- Thanks to my mentor for his guidance and support during our mentor meetings