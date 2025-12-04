from model import util
from model.crm import crm
from model.sales import sales
from view import terminal as view


# TODO
#   (8) Sum the price of transactions between two given dates.

def list_transactions():
    """Display a list of transactions."""
    transactions = sales.get_transactions()
    headers = sales.HEADERS
    table = [headers]
    for transaction in transactions:
        row = []
        for header in headers:
            row.append(transaction[header])
        table.append(row)
    view.print_table(table)
    view.wait_for_enter()


def add_transaction():
    """Add new transaction to the sales table."""
    transaction = {"customer": "",
                   "product": "",
                   "price": "",
                   "date": ""}

    is_valid_customer_id = False
    while not is_valid_customer_id:
        view.clear()
        view.print_message("Adding a new transaction")
        customer_id = view.get_input("Customer ID")
        if not customer_id:
            view.print_error_message("Customer ID cannot be empty. Please enter ID.")
        elif not crm.is_id_exist(customer_id):
            view.print_error_message("Customer ID does not exist. You need to add this customer first.")
        else:
            is_valid_customer_id = True
            transaction['customer'] = customer_id

    is_valid_product = False
    while not is_valid_product:
        view.clear()
        view.print_message("Adding a new transaction")
        product = view.get_input("Product name")
        if not product:
            view.print_error_message("Product name cannot be empty. Please enter a product name.")
        else:
            is_valid_product = True
            transaction['product'] = product

    is_valid_price = False
    while not is_valid_price:
        view.clear()
        view.print_message("Adding a new transaction")
        price = view.get_input("Price")
        try:
            float_price = float(price)
            if float_price < 0:
                view.print_error_message("Price cannot be negative. Please enter a valid price.")
            else:
                is_valid_price = True
                transaction['price'] = price
        except ValueError:
            view.print_error_message("Invalid price format. Please enter a numeric value.")

    transaction['date'] = util.get_current_time_iso_format()

    try:
        sales.add_transaction(transaction)
        view.clear()
        view.print_message("Adding a new transaction")
        view.print_message(f"Customer ID: {transaction['customer']}")
        view.print_message(f"Product: {transaction['product']}")
        view.print_message(f"Price: {transaction['price']}")
        view.print_message(f"Date: {transaction['date']}")
        view.print_message("Transaction added successfully.")
    except KeyError as err:
        view.print_error_message(err)
    view.wait_for_enter()


def update_transaction():
    """Update existing transaction in the sales table."""
    transaction = {"id": "",
                   "customer": "",
                   "product": "",
                   "price": "",
                   "date": ""}

    is_valid_transaction_id = False
    while not is_valid_transaction_id:
        view.clear()
        view.print_message("Updating a transaction")
        transaction_id = view.get_input("Transaction ID")
        if not transaction_id:
            view.print_error_message("Transaction ID cannot be empty. Please enter a valid ID.")
        elif not sales.is_id_exist(transaction_id):
            view.print_error_message("Transaction ID does not exist. Please enter a valid ID.")
        else:
            is_valid_transaction_id = True
            transaction = sales.get_transaction_by_id(transaction_id)

    is_valid_customer_id = False
    while not is_valid_customer_id:
        view.clear()
        view.print_message("Updating a transaction")
        customer_id = view.get_input("Customer ID")
        if not customer_id:
            is_valid_customer_id = True
        elif not crm.is_id_exist(customer_id):
            view.print_error_message("Customer ID does not exist. You need to add this customer first.")
        else:
            is_valid_customer_id = True
            transaction['customer'] = customer_id

    is_valid_product = False
    while not is_valid_product:
        view.clear()
        view.print_message("Updating a transaction")
        product = view.get_input("Product name")
        if not product:
            is_valid_product = True
        else:
            is_valid_product = True
            transaction['product'] = product

    is_valid_price = False
    while not is_valid_price:
        view.clear()
        view.print_message("Updating a transaction")
        price = view.get_input("Price")
        if not price:
            is_valid_price = True
        else:
            try:
                float_price = float(price)
                if float_price < 0:
                    view.print_error_message("Price cannot be negative. Please enter a valid price.")
                else:
                    is_valid_price = True
                    transaction['price'] = price
            except ValueError:
                view.print_error_message("Invalid price format. Please enter a numeric value.")

    is_valid_date = False
    while not is_valid_date:
        view.clear()
        view.print_message("Updating a transaction")
        date_str = view.get_input("Date (YYYY-MM-DD)")

        if not date_str:
            is_valid_date = True
        else:
            try:
                parsed_date = util.parse_date(date_str)
                is_valid_date = True
                transaction["date"] = parsed_date
            except ValueError:
                view.print_error_message("Invalid date. Please enter date in YYYY-MM-DD format.")

    try:
        sales.update_transaction(transaction)
        view.clear()
        view.print_message("Updating a transaction")
        view.print_message(f"Transaction ID: {transaction['id']}")
        view.print_message(f"Customer ID: {transaction['customer']}")
        view.print_message(f"Product: {transaction['product']}")
        view.print_message(f"Price: {transaction['price']}")
        view.print_message(f"Date: {transaction['date']}")
        view.print_message("Transaction added successfully.")
    except KeyError as err:
        view.print_error_message(err)
    view.wait_for_enter()


def delete_transaction():
    """Delete a transaction from the sales table."""
    transaction_id = ""
    is_valid_id = False
    while not is_valid_id:
        view.clear()
        view.print_message("Removing a transaction")
        transaction_id = view.get_input("Transaction ID")
        if not transaction_id:
            view.print_error_message("Transaction ID cannot be empty. Please enter a valid ID.")
        elif not sales.is_id_exist(transaction_id):
            view.print_error_message("Transaction ID does not exist. Please enter a valid ID.")
        else:
            is_valid_id = True

    try:
        sales.delete_transaction(transaction_id)
        view.clear()
        view.print_message("Removing a transaction")
        view.print_message(f"Transaction ID: {transaction_id}")
        view.print_message("Transaction removed successfully.")
    except KeyError as err:
        view.print_error_message(err)
    view.wait_for_enter()


def get_biggest_revenue_transaction():
    """Get the transaction that made the biggest revenue."""
    transactions = sales.get_transactions()
    if not transactions:
        view.print_message("No transactions available.")
        view.wait_for_enter()
        return

    # find maximum price (skip invalid/missing prices)
    max_price = None
    for transaction in transactions:
        try:
            price = float(transaction.get("price", ""))
        except (TypeError, ValueError):
            continue
        if max_price is None or price > max_price:
            max_price = price

    if max_price is None:
        view.print_message("No valid priced transactions found.")
        view.wait_for_enter()
        return

    # collect all transactions that have that max price
    top_transactions = []
    for transaction in transactions:
        try:
            if float(transaction.get("price", "")) == max_price:
                top_transactions.append(transaction)
        except (TypeError, ValueError):
            continue

    # display results
    if not top_transactions:
        view.print_message("No valid priced transactions found.")
    else:
        view.clear()
        view.print_message(f"Transaction(s) with the biggest revenue ({max_price}).")
        for transaction in top_transactions:
            view.print_message(f"Transaction ID: {transaction['id']}")
    view.wait_for_enter()


def get_biggest_revenue_product():
    """Get the product that made the biggest revenue altogether."""
    transactions = sales.get_transactions()
    products = {}
    for transaction in transactions:
        product = transaction.get("product", "")
        try:
            price = float(transaction.get("price", ""))
        except (TypeError, ValueError):
            continue
        if product in products:
            products[product] += price
        else:
            products[product] = price

    # display results
    if not products:
        view.print_message("No products found.")
    else:
        max_revenue = max(products.values())
        top_products = [product for product, revenue in products.items() if revenue == max_revenue]
        view.clear()
        view.print_message(f"Product(s) with the biggest revenue ({max_revenue}):")
        for product in top_products:
            view.print_message(f"- {product}")
    view.wait_for_enter()


def count_transactions_between():
    """Count number of transactions between two given dates."""
    transactions = sales.get_transactions()

    start_date_str = ""
    is_valid_start_date = False
    while not is_valid_start_date:
        view.clear()
        view.print_message("Counting transactions between two dates")
        start_date_str = view.get_input("Start Date (YYYY-MM-DD)")

        if not start_date_str:
            view.print_error_message("Start date cannot be empty. Please enter a valid date.")
        else:
            try:
                start_date_str = util.parse_date(start_date_str)
                is_valid_start_date = True
            except ValueError:
                view.print_error_message("Invalid date. Please enter date in YYYY-MM-DD format.")

    end_date_str = ""
    is_valid_end_date = False
    while not is_valid_end_date:
        view.clear()
        view.print_message("Counting transactions between two dates")
        end_date_str = view.get_input("Start Date (YYYY-MM-DD)")

        if not end_date_str:
            view.print_error_message("Start date cannot be empty. Please enter a valid date.")
        else:
            try:
                end_date_str = util.parse_date(end_date_str)
                is_valid_end_date = True
            except ValueError:
                view.print_error_message("Invalid date. Please enter date in YYYY-MM-DD format.")

    count_transactions = 0
    for transaction in transactions:
        transaction_date = transaction.get("date", "")
        if start_date_str <= transaction_date <= end_date_str:
            count_transactions += 1

    view.clear()
    view.print_message("Counting transactions between two dates")
    view.print_message(f"Number of transactions between {start_date_str} and {end_date_str}: {count_transactions}")
    view.wait_for_enter()


def sum_transactions_between():
    view.print_error_message("Not implemented yet.")


def run_operation(option):
    if option == 1:
        list_transactions()
    elif option == 2:
        add_transaction()
    elif option == 3:
        update_transaction()
    elif option == 4:
        delete_transaction()
    elif option == 5:
        get_biggest_revenue_transaction()
    elif option == 6:
        get_biggest_revenue_product()
    elif option == 7:
        count_transactions_between()
    elif option == 8:
        sum_transactions_between()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List transactions",
               "Add new transaction",
               "Update transaction",
               "Remove transaction",
               "Get the transaction that made the biggest revenue",
               "Get the product that made the biggest revenue altogether",
               "Count number of transactions between",
               "Sum the price of transactions between"]
    view.print_menu("Sales", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
