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

sales = SHEET.worksheet('sales')

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

        data_str = input('Please enter Cheese, Ham and Sausage sales for today here:\n')

        sales_data = data_str.split(",")

        
        print("Thank you, the data you have entered is valid")
        break

    return sales_data

get_sales_data()



