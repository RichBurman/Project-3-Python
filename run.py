import gspread, re
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

CHEESE_PIZZA_COST = 8  # Cheese Pizza Cost is £8
HAM_PIZZA_COST = 9     # Ham Pizza Cost is £9
SAUSAGE_PIZZA_COST = 10  # Sausage Pizza Cost is £10



# Function to enter valid date and sales data

def enter_sales_data():
    """
    1. This allows the user to input the date of the sales data, in a format of "YYYY-MM-DD". 
    2. This is validated to show it matches the correct date format. 
    3. The sales data entered with by 3 types of pizza, Cheese, Ham and Sausage. The numbers entered
    by the user must be non-negative, otherwise the loop will display an error message. 
    4. Once data entered is valid, the function will create a list which contains the date, cheese sales, 
    ham sales and sausage sales. 
    5. This will access the "sales" worksheet and update a new row in the sales data. 
    6. A message is displayed to the user to inform them that sales data was enter and stored successfully. 
    7. This will calculate the daily profit on all 3 types of pizza and update the profit worksheet. This 
    takes the sales data for a pizza type and muliples it by it's pizza cost, e.g. Cheese £8 x 30 Cheese Pizza sales. 
    This will do the same for all 3 types of pizza and then in the last column add all the 3 profits together to produce
    a total profit for the day. 
    """
    print(" Please enter the Sales Data for today.\n")

    # Validate date format (YYYY-MM-DD)
    while True:
        date = input("Enter the date (YYYY-MM-DD): ")
        if re.match(r"^\d{4}-\d{2}-\d{2}$", date):
            break
        else:
            print("Invalid date format. Please use YYYY-MM-DD format.")

    # Validate sales values
    while True:
        try:
            cheese_sales = int(input("Enter Cheese Pizza sales: "))
            ham_sales = int(input("Enter Ham Pizza sales: "))
            sausage_sales = int(input("Enter Sausage Pizza sales: "))
            
            if cheese_sales >= 0 and ham_sales >= 0 and sausage_sales >= 0:
                break
            else:
                print("Sorry, Sales values must be non-negative integers.")
        except ValueError:
            print("Sorry, Invalid input. Please enter valid integers for sales.")

    # Update sales data to the worksheet
    sales_data = [date, cheese_sales, ham_sales, sausage_sales]
    SHEET.worksheet("sales").append_row(sales_data)
    print("The Sales data has been entered successfully and been added to the Sales Worksheet!\n")

    # Calculates profit for each pizza type and a total profit all sales of pizza that day
    cheese_profit = cheese_sales * CHEESE_PIZZA_COST
    ham_profit = ham_sales * HAM_PIZZA_COST
    sausage_profit = sausage_sales * SAUSAGE_PIZZA_COST
    total_profit = cheese_profit + ham_profit + sausage_profit
    profit_sheet = SHEET.worksheet("profit")
    profit_sheet.append_row([date, cheese_profit, ham_profit, sausage_profit, total_profit])
    print("Profit and loss worksheet has been updated successfully!\n")

    # Update the stock levels after the sales data has been entered. (Stock item level - item sales)

    stock_sheet = SHEET.worksheet("stock")
    current_stock = stock_sheet.get_all_values()[-1]

    try:
        new_stock = [
            int(current_stock[0]) - cheese_sales,
            int(current_stock[1]) - ham_sales,
            int(current_stock[2]) - sausage_sales
        ]
    except ValueError:
        print("Error: Invalid stock data. Please check the stock worksheet for correct values.")

    stock_sheet.append_row(new_stock)
    print("Stock updated successfully!\n")

    # Check current stock levels and if any stock item is below 50 items, informs user and advises ordering new stock.
    stock_threshold = 50
    for item, new_quantity, stock_value in zip(["Cheese Pizzas", "Ham Pizzas", "Sausage Pizzas"], new_stock, new_stock):
        if new_quantity < stock_threshold:
            print(f"{item} are running low (stock: {new_quantity}) You may want to consider ordering more stock.")



def order_new_stock():
    """
    This function allows the user to order new stock for each type of pizza (This will add on to the existing stock) and updates the stock worksheet.
    """
    print("Order New Stock\n")

    stock_sheet = SHEET.worksheet("stock")
    current_stock = stock_sheet.get_all_values()[-1]
    
    print("Current Stock Levels:")
    print(f"Cheese Pizzas in Stock: {current_stock[0]}")
    print(f"Ham Pizzas in Stock: {current_stock[1]}")
    print(f"Sausage Pizzas in Stock: {current_stock[2]}")
    
    
    cheese_qty = int(input("Enter quantity of Cheese Pizzas to order: "))
    ham_qty = int(input("Enter quantity of Ham Pizzas to order: "))
    sausage_qty = int(input("Enter quantity of Sausage Pizzas to order: "))

    stock_sheet = SHEET.worksheet("stock")
    current_stock = stock_sheet.get_all_values()[-1]
    
    new_stock = [
        int(current_stock[0]) + cheese_qty,
        int(current_stock[1]) + ham_qty,
        int(current_stock[2]) + sausage_qty
    ]
    
    # Displays to the user that the stock has been updated. 
    stock_sheet.append_row(new_stock)
    print("New stock ordered successfully and the stock worksheet has been updated!\n")
    print("Here are the updated stock levels:\n")
    print(f"Cheese Pizzas in Stock: {new_stock[0]}")
    print(f"Ham Pizzas in Stock: {new_stock[1]}")
    print(f"Sausage Pizzas in Stock: {new_stock[2]}")

    # Update the current_stock with the new stock values so user can see stock has been updated
    current_stock = new_stock


def view_stock_levels():
    """
    This function allows the user to view the current stock levels for all 3 types of pizza. 
    """
    print("View Current Stock Levels\n")
    stock_data = SHEET.worksheet("stock").get_all_values()[-1]
    print(f"Cheese Pizzas in Stock: {stock_data[0]}")
    print(f"Ham Pizzas in Stock: {stock_data[1]}")
    print(f"Sausage Pizzas in Stock: {stock_data[2]}")


# Daily Sales Report

def sales_report():
    print("Sales Report\n")
    sales_data = SHEET.worksheet("sales").get_all_values()
    for row in sales_data:
        date = row[0]
        cheese_sales = row[1]
        ham_sales = row[2]
        sausage_sales = row[3]
        print(f"Date: {date}\n")
        print(f"Cheese Pizza Sales: {cheese_sales}")
        print(f"Ham Pizza Sales: {ham_sales}")
        print(f"Sausage Pizza Sales: {sausage_sales}\n")
        print("-" * 30)

sales_report()


# def user_menu():
#     while True:
#         print("Welcome to Pizza World")
#         print("1. Enter Sales Data")
#         print("2. Order New Stock")
#         print("3. View Current Stock Levels")
#         print("4. Quit\n")
#         choice = input("Enter your choice: ")
#         if choice == "1":
#             enter_sales_data()
#         elif choice == "2":
#             order_new_stock()
#         elif choice == "3":
#             view_stock_levels()
#         elif choice == "4":
#             print("Goodbye!")
#             break
#     else:
#         print("Invalid choice. Please select a valid option.\n")

# user_menu()








  



# def get_sales_data():

#     """
#     Get sales for the 3 types of pizza.
#     This will be inputted by the user.
#     This will run a while loop to collect valid data
#     from the user via the terminal.
#     Data must be a string of 3 numbers seperated by commas.
#     The loop will continue to request
#     data until it is valid.
#     """

#     while True:
#         print("Welcome to Pizza World sales!")
#         print("Please enter sales for Cheese, Ham and Sausage")
#         print("Please enter 3 numbers, which are seperated by commas")
#         print("Example: 10,10,10\n")

#         data_str = input('Please enter Cheese, Ham and Sausage sales:\n')

#         sales_data = data_str.split(",")

#         if valid_data(sales_data):
#             print("Thank you, the data you have entered is valid")
#             break

#     return sales_data
    
    
# def valid_data(values):
#     """
#     Checks all data inputted by the user for the sales of pizza is valid.
#     Converts all string values into integers (to transfer to google worksheet)
#     ValueError raised if string can not be coverted into integer and/or if
#     3 values not entered by the user.
#     """

#     try:
#         [int(value) for value in values]
#         if len(values) != 3:
#             raise ValueError(
#                 f"Please ensure you enter 3 values, you entered {len(values)}"
#             )
#     except ValueError as e:
#         print(f"Invalid data entered: {e}, please try again.\n")
#         return False
#     return True


# def update_worksheet(data, worksheet):
#     """
#     Takes the user entered integers to be sent to the google worksheet
#     Updates the worksheet with the valid data provided by the user
#     Updates user via terminal that data been sent succesfully to worksheet
#     """
#     print(f"Updating {worksheet} worksheet with daily pizza sales...\n")
#     worksheet_to_update = SHEET.worksheet(worksheet)
#     worksheet_to_update.append_row(data)
#     print(f"The {worksheet} worksheet updated successfully\n")


# def calculate_surplus_data(sales_row):
#     """
#     Takes sales data and subtracts from stock
#     to provide the surplus for each pizza

#     Positive number in surplus shows wasted pizzas
#     Negative number in surplus shows extra pizzas were made during day
#     """
#     print("Calculating surplus pizza data...\n")
#     stock = SHEET.worksheet("stock").get_all_values()
#     stock_row = stock[-1]

#     surplus_data = []
#     for stock, sales in zip(stock_row, sales_row):
#         surplus = int(stock) - sales
#         surplus_data.append(surplus)
#     return surplus_data


# def add_stock_data():
#     """
#     Add the daily stock for each pizza type
#     Company makes 20 of each pizza daily
#     """
#     print("Adding new stock data...\n ")

#     stock = SHEET.worksheet("stock")

#     new_stock_data = []
#     daily_stock = [20, 20, 20]
#     stock.append_row(daily_stock)

#     return new_stock_data


# def profit_pizza():
#     """
#     Calculate the profit made per pizza
#     Pizza:
#     Cheese Pizza - £5 per pizza
#     Ham Pizza - £8 per pizza
#     Sausage Pizza - £10 per pizza
#     """

#     print("Adding new profit data...\n ")
#     profits = SHEET.worksheet("sales").get_all_values()
#     profit_row = profits[-1]

#     cheese_profits = int(profit_row[0]) * 5
#     ham_profits = int(profit_row[1]) * 8
#     sausage_profits = int(profit_row[2]) * 10

#     profit_data = [cheese_profits, ham_profits, sausage_profits]

#     return profit_data


# def main_program():
#     """
#     Runs all program functions and displays prints to user with
#     - sales for the day
#     - profit for the day
#     - total profit for the day
#     """
#     data = get_sales_data()
#     sales_data = [int(num) for num in data]
#     update_worksheet(sales_data, "sales")
#     new_surplus_data = calculate_surplus_data(sales_data)
#     update_worksheet(new_surplus_data, 'surplus')
#     stock_data = add_stock_data()
#     update_worksheet(stock_data, "stock")
#     profit_data = profit_pizza()
#     update_worksheet(profit_data, "profit")
#     row_profit = sum(profit_data)
#     print("Today Pizza Figures!!!\n")
#     print(f"Sales Today {sales_data}\n")
#     print(f"Profit Today {profit_data}\n")
#     print(f"Total Daily Profit £{row_profit}\n")


# main_program()