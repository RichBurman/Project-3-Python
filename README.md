![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# PizzaWorld 

PizzaWorld is a Python terminal program which runs in the Code Insitute mock terminal on Heroku. 

PizzaWorld is designed for a Pizza company which sells 3 types of pizza
- Cheese Pizza
- Ham Pizza 
- Sausage Pizza

PizzaWorld allows the users to :
- Input the daily sales of the 3 types of pizza
- Upload sales to a googlesheet
- Update the new stock levels for the next day
- Upload stock levels to a googlesheet
- Calculate the surplus of pizzas from the day and show any pizzas that were wasted
- Upload the surplus to a googlesheet
- Calculate profit made on the different types of pizza with different profit margins
- Upload the profit of each type of pizza to a googlesheet
- Displays to the user the total sales of each pizza for the day
- Displays to the user the profit per pizza for the day
- Displays the total profit made from all pizza sales for the day

## How it works

PizzaWorld allows the user to input the daily sales data of the 3 types of pizzas (Cheese, Ham and Sausage) sold during the day. 

The user inputs the 3 sales data e.g. 15, 17, 19 and press enter. 

This sends the sales data to a google worksheet and stores the sales figures for the business. 

PizzaWorld uses the sales data to provide the user with key business information on the following areas: 

- Stock - The pizza business produce 20 of each pizzas at the start of everyday. This data is stored in the google worksheet.
- Surplus - The sales data is subtracted from the stock and informs the pizza business how many pizzas were wasted that day or how many extra they had to make extra during the day. This data is stored in the google worksheet.
- Profit - Each pizza provides a different level of profit
    - Cheese pizza provides £5.00 profit per pizza
    - Ham pizza provides £8.00 profit per pizza
    - Sauasge pizza provides £10.00 profit per pizza

    Pizzaworld takes the sales data and calculates the profit for each type of pizza and stores this data in the google worksheet. 

    <img src="assets/images/README/all_sheets.png" width="300" height="50" alt="Image of accepting data"> 

The user is informed via the terminal what processes PizzaWorld has completed and what areas of the google worksheet have been updated with new data. 

<img src="assets/images/README/updates.png" width="400" height="400" alt="Image of accepting data"> 
    
Once all these functions have been performed, the user is provided with, via the terminal a print out of the following: 

- Sales data for the day
- Profit per pizza for the day
- Total profit of all pizza sold for the day

    <img src="assets/images/README/print.png" width="150" height="150" alt="Image of print"> 

PizzaWorld provies the user with a tool, that allows them to store sales data, calculate and store stock and surplus levels, provides and stores profits for the types of pizza sold and provides the total profit made by the business. 


## Features
- Existing Features
    - Sales Data Entry
        - User is welcomed and asked to enter sales data for the 3 types of pizza (Cheese, Ham, Sausage) 
        - User is provided with clear instructions of how the sales data must be entered and an example is provided. 
    
            <img src="assets/images/README/sales_data_entry.png" width="300" height="100" alt="Image of sales data entry"> 

        - Accepts user data 
        - Informs user that the data enter is valid

            <img src="assets/images/README/accepts_data.png" width="300" height="100" alt="Image of accepting data"> 

        - Input validation and error-checking
            - You must enter numbers
            - You can not enter blank spaces
            - You must enter 3 numbers

            <img src="assets/images/README/validation_and_error_checks.png" width="500" height="250" alt="Image of accepting data"> 

        - Loop in place to return user to data input to allow for user to attempt to enter valid data.

- Future Features
    - Allow user to adjust stock levels via the terminal
    - Allow user to adjust individual pizza pricing via the terminal
    - Add date to google worksheet and allow user to search via terminal for specific sales data entries
    - Add function that allows user to see the total profit for week, month, year
    - Add function to allow user to add new pizza (Name, profit) and update to google worksheet
    - 
## Data Model
- Flowchart plan
    - I decided to use a Flowchart plan to model how I wanted Pizzaworld to function. 
    - It allowed me to clearly see the path I wanted to follow when designing and creating Pizzaworld. 
    - It allowed me to ensure all areas of PizzaWorld positioned correctly and ensured I had a blueprint to follow in order to produce a fully functioning program. 
    - I wanted the store all the data inputted and created from PizzaWorld into a worksheet to allow the user to store the data to aid with future business decisions (Which pizzas are popular, whether more stock is needed for a particular pizza on a daily basis, which pizzas are providing the business with the most profit)

    <img src="assets/images/README/flowchart.png" width="500" height="400" alt="Image of Flowchart"> 


## Testing

I have manually tested this project by doing the following:

    - Passed the code through a PEP8 linter and confirmed there are no problems
    - Given invalid inputs: strings when numbers are expected, more than 3 numbers
    - Tested in my local terminal and the Code Institue Heroku terminal

<img src="assets/images/README/validation_and_error_checks.png" width="500" height="250" alt="Image of accepting data"> 


 ## Bugs
### Solved Bugs

- I was receiving error index because I had forgotten to add 'int' at the start of the various (profit_row). I fixed this by adding 'int' to all of the profit_row variables, which allowed the calculation to take place.
<img src="assets/images/README/solved_bug.png" width="500" height="250" alt="Image of accepting data"> 


### Remaining Bugs

- No bugs remaining

## Validator Testing

- PEP8
    - No errors were returned from pep8ci.herokuapp.com

## Deployment


## Credits

    - Code Institute for the deployment terminal 
    - Thanks to my mentor for his guidance and support during our mentor meetings