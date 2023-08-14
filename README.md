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

<img src="assets/images/README/menu.png" width="500" height="400" alt="Image of Flowchart"> 

Pizza World welcomes users to it's menu. This allows users to select out of 8 options depending on what function they would like to perform

1. Enter Sales Data
 2. Order New Stock
 3. View Current Stock Levels
 4. View Sales Report (Shows all sales data)
 5. View Profit Report
 6. Search for sales data by date
 7. View the most profitable pizza
 8. Quit

The user has to enter the number of their choice. It must be a number between 1-8 otherwise it will fail validation checks and the user is returned to the menu. 

<img src="assets/images/README/menu_valid.png" alt="Image of Flowchart"> 


#### 1 Enter Sales Data

The function allows the user to enter the sales data for the 3 pizzas, the user can select the date for the sales data to be assigned to. 

First the user has to enter the date for the data. 

<img src="assets/images/README/sales_data_date.png"  alt="Image of Flowchart"> 

Once the user has entered the date, the user inputs the sales data for each type of pizza. 

<img src="assets/images/README/sales_data_enter.png" alt="Image of Flowchart"> 

Once this data has been inputted correctly, the user is informed that all data has been entered successfully and the Sales worksheet has been updated with the data. 

In addition to this, the profit and loss worksheet has been updated successfully, as this calculates the number of pizzas sold by their respectively cost and this data, along with the total profit from the sale of all pizzas for that entry is saved in the profit worksheet. 

Finally the stock worksheet is updated. The numbers of pizzas that were inputted in the sales date for each pizza is subtracted from the respective stock of that type of pizza and updates the stock number, to show how much stock is remaining of each pizza. 

<img src="assets/images/README/sales_data_success.png" alt="Image of Flowchart"> 

##### If stock levels are lower than 50 when sales data entered

After a user has inputted the sales data successfully, if stock levels for a pizza has dropped below 50, a message will print to inform the user than the current stock on that particular pizza is low and they may want to consider ordering more stock. 

<img src="assets/images/README/low_stock.png" alt="Image of Flowchart"> 

#### 2 Order New Stock

This function allows the user to order new stock for each pizza type. 

It display to the user the following:

- Current stock levels - so the user can use this information to decide how much new stock they wish to order
- Input box to allow them to enter how much new stock for each pizza they would like. This data must be entered correctly to meet validation requirements. 

<img src="assets/images/README/order_stock.png" alt="Image of ordering stock"> 


Once this data has been inputted. The user is informed that the New stock has been ordered successfully and the stock worksheet has been updated. 

In addition to this, the updated stock levels are displayed to the user, show they can see the new stock levels for each pizza type.

##### Updated Stock Image

<img src="assets/images/README/updated_stock.png" alt="Image of Updated stock"> 

#### View Current Stock Levels

This function allows the user to view the current stock levels of all 3 pizza types. It will display the stock levels of all pizzas and return the user to the user menu. 

<img src="assets/images/README/view_stock.png" alt="Image of Updated stock"> 








- Future Features

 - When a user inputs the sales data and stock levels drop below 50, an option for the user to order new stock to appear and perform the function, without having to access new order from the user menu. 


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
<img src="assets/images/README/solved_bug.png" width="150" height="300" alt="Image of solved bug"> 


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