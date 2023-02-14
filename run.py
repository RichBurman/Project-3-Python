import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('pizza_world')

def get_sales_data():

    """
    Get sales for the 3 types of pizza. This will be inputted by the user. 
    This will run a while loop to collect valid data from the user via the terminal.
    Data must be a string of 3 numbers seperated by commas. The loop will continue to request
    data until it is valid.
    """

    while True:
        print("Welcome to Pizza World sales!")
        print("Please enter sales for Cheese, Ham and Sausage Pizzas")
        print("Please enter 3 numbers, which are seperated by commas")
        print("Example: 10,10,10\n")

        data_str = input('Please enter Cheese, Ham and Sausage sales for today:\n')

        sales_data = data_str.split(",")

        if valid_data(sales_data):
            print("Thank you, the data you have entered is valid")
            break

    return sales_data



def valid_data(values):
    """
    Checks all data inputted by the user for the sales of pizza is valid. 
    Converts all string values into integers (to transfer to google worksheet)
    ValueError raised if string can not be coverted into integer and/or if 
    3 values not entered by the user. 
    """

    try:
        [int(value) for value in values]
        if len(values) != 3:
            raise ValueError(
                f"Please ensure you enter 3 values, you entered {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data entered: {e}, please try again.\n")
        return False
    return True

def update_worksheet(data, worksheet):
    """
    Takes the user entered integers to be sent to the google worksheet
    Updates the worksheet with the valid data provided by the user
    Updates user via terminal that data been sent succesfully to worksheet
    """
    print(f"Updating {worksheet} worksheet with daily pizza sales...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"The {worksheet} worksheet updated successfully\n")

def calculate_surplus_data(sales_row):
    """
    Takes sales data and subtracts from stock to provide the surplus for each pizza

    Positive number in surplus shows wasted pizzas
    Negative number in surplus shows extra pizzas were made during day 
    """
    print("calculating surplus pizza data...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]

    surplus_data = []
    for stock, sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales
        surplus_data.append(surplus)
    
    return surplus_data

def mainprogram():
    """
    Runs all program functions
    """
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_worksheet(sales_data, "sales")
    new_surplus_data = calculate_surplus_data(sales_data)
    update_worksheet(new_surplus_data, 'surplus')

mainprogram()
