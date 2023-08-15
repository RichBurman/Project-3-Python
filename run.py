import gspread
import re
import datetime
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
    8. The sales data entered for each pizza type will be subtracted from the current stock level of that pizza type and this will be
    updated in the stock worksheet. If the stock level for any pizza type goes below 50 items, a print message will inform
    the user that the current stock is low and they may wish to place a new order.
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
    # Show current stock
    print("Current Stock Levels:")
    print(f"Cheese Pizzas in Stock: {current_stock[0]}")
    print(f"Ham Pizzas in Stock: {current_stock[1]}")
    print(f"Sausage Pizzas in Stock: {current_stock[2]}")

    # Function to get valid integer input only!
    def get_valid_input(prompt):
        while True:
            try:
                value = int(input(prompt))
                if value < 0:
                    print("Please enter a non-negative value.")
                else:
                    return value
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
    
    # User inputs stock to order using get_valid_input()
    cheese_qty = get_valid_input("Enter quantity of Cheese Pizzas to order: ")
    ham_qty = get_valid_input("Enter quantity of Ham Pizzas to order: ")
    sausage_qty = get_valid_input("Enter quantity of Sausage Pizzas to order: ")

    # Updates stock worksheet
    stock_sheet = SHEET.worksheet("stock")
    current_stock = stock_sheet.get_all_values()[-1]
    # Displays new stock levels
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

    # Update the current_stock with the new stock values so the user can see stock has been updated
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
    """
    This function allows the user to view all the entered sales data record from the sales data worksheet.
    """
    print("Sales Report\n")
    sales_data = SHEET.worksheet("sales").get_all_values()
    for row in sales_data:
        date = row[0]
        cheese_sales = row[1]
        ham_sales = row[2]
        sausage_sales = row[3]
        print(f"{date:<15}{cheese_sales:<15}{ham_sales:<15}{sausage_sales:<15}")
        print("-" * 60)

# Profit and Loss


def profit_loss_report():
    """
    This function allows the user to view all profits or losses made by each pizza type and the total profit overall.
    """
    print("Profit and Loss Report\n")
    profits = SHEET.worksheet("profit").get_all_values()
    total_profit = 0
    print(f"{'Date':<15}{'Cheese':<15}{'Ham':<15}{'Sausage':<15}{'Total':<15}")
    print("=" * 70)
    for profit_row in profits[1:]:
        date = profit_row[0]
        cheese_profit = int(profit_row[1])
        ham_profit = int(profit_row[2])
        sausage_profit = int(profit_row[3])
        daily_total_profit = int(profit_row[4])
        print(f"{date:<15}{cheese_profit:<15}{ham_profit:<15}{sausage_profit:<15}{daily_total_profit:<15}")
        total_profit += daily_total_profit
    print("=" * 70)
    print(f"{'Total Profit:':<60}{total_profit:>10}\n")

# Search for sales data by date


def search_sales_by_date():
    """
    This function allows the user to search for sales data from a specific date inputted by the user. 
    """
    print("Search Sales Data by Date\n")
    
    # Function to get valid date input
    def get_valid_date_input(prompt):
        while True:
            try:
                date_input = input(prompt)
                datetime.datetime.strptime(date_input, '%Y-%m-%d')
                return date_input
            except ValueError:
                print("Invalid date format. Please enter a date in the format YYYY-MM-DD.")
    
    target_date = get_valid_date_input("Enter the date (YYYY-MM-DD): ")
    sales_data = SHEET.worksheet('sales').get_all_values()
    found_data = False 

    for row in sales_data:
        date = row[0]
        if date == target_date:
            cheese_sales = row[1]
            ham_sales = row[2]
            sausage_sales = row[3]
            print(f"Date: {date}\n")
            print(f"Cheese Pizza Sales: {cheese_sales}")
            print(f"Ham Pizza Sales: {ham_sales}")
            print(f"Sausage Pizza Sales: {sausage_sales}\n")
            print("-" * 30)
            found_data = True
            break
    if not found_data:
        print(f"No sales data found for that date")


def most_profitable_pizza():
    """
    This function allows the user to see which pizza has made the most profit, out of Cheese, Ham and Sausage. It also displays how much profit overall that pizza has made for Pizza World.
    """
    print("Most Profitable Pizza Type\n")
    profits = SHEET.worksheet("profit").get_all_values()
    
    pizza_types = ["Cheese", "Ham", "Sausage"]
    pizza_profits = [0, 0, 0]
    
    for profit_row in profits[1:]:
        for i, profit in enumerate(profit_row[1:4]):
            pizza_profits[i] += int(profit)
    
    max_profit = max(pizza_profits)
    most_profitable_index = pizza_profits.index(max_profit)
    most_profitable_pizza = pizza_types[most_profitable_index]
    
    print("Profit made by each pizza type:")
    print("-" * 30)
    for i, pizza_type in enumerate(pizza_types):
        print(f"{pizza_type}: £{pizza_profits[i]}")

    print("-" * 30)
    print("\nThe most profitable pizza type is:", most_profitable_pizza)
    print(f"Total profit made by the most profitable pizza: £{max_profit}")


def user_menu():
    while True:
        print("Welcome to Pizza World")
        print("1. Enter Sales Data")
        print("2. Order New Stock")
        print("3. View Current Stock Levels")
        print("4. View Sales Report (Shows all sales data)")
        print("5. View Profit Report")
        print("6. Search for sales data by date")
        print("7. View the most profitable pizza")
        print("8. Quit\n")
        choice = input("Enter your choice: ")
        if choice == "1":
            enter_sales_data()
        elif choice == "2":
            order_new_stock()
        elif choice == "3":
            view_stock_levels()
        elif choice == "4":
            sales_report()
        elif choice == "5":
            profit_loss_report()
        elif choice == "6":
            search_sales_by_date()
        elif choice == "7":
            most_profitable_pizza()
        elif choice == "8":
            print("Goodbye! Thank you for using Pizza World!")
            break
        else:
            print("Invalid choice. Please select a valid option.\n")


user_menu()
