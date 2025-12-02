from model.crm import crm
from view import terminal as view


def list_customers():
    """Display all customers in the CRM table."""
    customers = crm.get_customers()
    headers = list(customers[0].keys())
    table = [headers]
    for customer in customers:
        row = []
        for header in headers:
            row.append(customer[header])
        table.append(row)
    view.print_table(table)
    view.wait_for_enter()


def add_customer():
    """Add new customer to the CRM table."""
    customer = {"name": "",
                "email": "",
                "subscribed": ""}

    is_valid_name = False
    while not is_valid_name:
        view.clear()
        view.print_message("Adding a new customer")
        name = view.get_input("Name").capitalize()
        if not name:
            view.print_error_message("Name cannot be empty. Please enter a valid name.")
        elif any((not char.isalnum() and char not in [" ", "-", "."]) for char in name):
            view.print_error_message("Name contains invalid characters. Please enter a valid name.")
        else:
            is_valid_name = True
            customer['name'] = name

    is_valid_email = False
    while not is_valid_email:
        view.clear()
        view.print_message("Adding a new customer")
        view.print_message(f"Name: {customer['name']}")
        email = view.get_input("Email")
        if "@" not in email or "." not in email.split("@")[-1]:
            view.print_error_message("Invalid email format. Please enter a valid email address.")
        else:
            is_valid_email = True
            customer['email'] = email

    is_valid_subscribed = False
    while not is_valid_subscribed:
        view.clear()
        view.print_message("Adding a new customer")
        view.print_message(f"Name: {customer['name']}")
        view.print_message(f"Email: {customer['email']}")
        subscribed = view.get_input("Subscribed (1: yes, 0: no)")
        if subscribed not in ["0", "1"]:
            view.print_error_message("Subscribed must be 1 (yes) or 0 (no). Please enter a valid value.")
        else:
            is_valid_subscribed = True
            customer['subscribed'] = subscribed

    crm.add_customer(customer)
    view.clear()
    view.print_message("Adding a new customer")
    view.print_message(f"Name: {customer['name']}")
    view.print_message(f"Email: {customer['email']}")
    view.print_message(f"Subscribed: {customer['subscribed']}")
    view.print_message("New customer added.")
    view.wait_for_enter()


def update_customer():
    """Update existing customer in the CRM table."""
    customer = {"id": "",
                "name": "",
                "email": "",
                "subscribed": ""}

    is_valid_id = False
    while not is_valid_id:
        view.clear()
        view.print_message("Updating a customer")
        customer_id = view.get_input("Customer ID")
        if not customer_id:
            view.print_error_message("Customer ID cannot be empty. Please enter a valid ID.")
        elif not crm.is_id_exist(customer_id):
            view.print_error_message("Customer ID does not exist. Please enter a valid ID.")
        else:
            is_valid_id = True
            customer = crm.get_customer_by_id(customer_id)

    is_valid_name = False
    while not is_valid_name:
        view.clear()
        view.print_message("Updating a customer")
        name = view.get_input("Name").capitalize()
        if not name:
            # Keep existing name if input is empty
            is_valid_name = True
        elif any((not char.isalnum() and char not in [" ", "-", "."]) for char in name):
            view.print_error_message("Name contains invalid characters. Please enter a valid name.")
        else:
            is_valid_name = True
            customer['name'] = name

    is_valid_email = False
    while not is_valid_email:
        view.clear()
        view.print_message("Updating a customer")
        view.print_message(f"Name: {customer['name']}")
        email = view.get_input("Email")
        if not email:
            # Keep existing email if input is empty
            is_valid_email = True
        elif "@" not in email or "." not in email.split("@")[-1]:
            view.print_error_message("Invalid email format. Please enter a valid email address.")
        else:
            is_valid_email = True
            customer['email'] = email

    is_valid_subscribed = False
    while not is_valid_subscribed:
        view.clear()
        view.print_message("Updating a customer")
        view.print_message(f"Name: {customer['name']}")
        view.print_message(f"Email: {customer['email']}")
        subscribed = view.get_input("Subscribed (1: yes, 0: no)")
        if not subscribed:
            # Keep existing subscribed status if input is empty
            is_valid_subscribed = True
        elif subscribed not in ["0", "1"]:
            view.print_error_message("Subscribed must be 1 (yes) or 0 (no). Please enter a valid value.")
        else:
            is_valid_subscribed = True
            customer['subscribed'] = subscribed

    crm.update_customer(customer)
    view.clear()
    view.print_message("Updating a customer")
    view.print_message(f"Name: {customer['name']}")
    view.print_message(f"Email: {customer['email']}")
    view.print_message(f"Subscribed: {customer['subscribed']}")
    view.print_message("Customer updated.")
    view.wait_for_enter()


def delete_customer():
    """Delete a customer from the CRM table."""
    customer_id = ""
    is_valid_id = False
    while not is_valid_id:
        view.clear()
        view.print_message("Delete a customer")
        customer_id = view.get_input("Customer ID")
        if not customer_id:
            view.print_error_message("Customer ID cannot be empty. Please enter a valid ID.")
        elif not crm.is_id_exist(customer_id):
            view.print_error_message("Customer ID does not exist. Please enter a valid ID.")
        else:
            is_valid_id = True

    crm.delete_customer_by_id(customer_id)
    view.clear()
    view.print_message('Delete a customer')
    view.print_message(f"Customer with ID {customer_id} has been deleted.")
    view.wait_for_enter()


def get_subscribed_emails():
    view.print_error_message("Not implemented yet.")


def run_operation(option):
    if option == 1:
        list_customers()
    elif option == 2:
        add_customer()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List customers",
               "Add new customer",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails"]
    view.print_menu("Customer Relationship Management", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
        except ValueError:
            view.print_error_message("Please enter a number!")
