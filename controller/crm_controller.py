from model.crm import crm
from view import terminal as view
from model import util

def list_customers():
    #view.print_error_message("Not implemented yet.")
    for customer in crm.customers:
        print(customer.name)

def add_customer():
    #view.print_error_message("Not implemented yet.")
    import re
    name = input("Username: ")
    valid_email = False
    while valid_email != True:
        email = input("E-mail: ")
        
        if re.match("\A(?P<name>[\w\-_]+)@(?P<domain>[\w\-_]+).(?P<toplevel>[\w]+)\Z",email,re.IGNORECASE):
            valid_email = True
        else:
            print("Invalid e-mail adress!")

    subsribed_status = input("Is %s subsribed? (y/n) "%name)

    if subsribed_status == "y":
        subsribed = 1
    elif subsribed_status == "n":
        subsribed = 0
    print("%s's user ID is:"%name, util.generate_id(10))


def update_customer():
    #view.print_error_message("Not implemented yet.")
    #ask_user_id = input("Please insert the user's ID you'd like to update: ")
    #if ask_user_id in crm.crm_data_list:
    #    new_name = input("New name: ")
    #    name = new_name
    #    new_email = input("New email: ")
    #    email = new_email
    #    subsribed_status = input("Is %s subsribed? (y/n) "%name)
    #    new_subsribed = 0
    #    if subsribed_status == "y":
    #        new_subsribed = 1
    #    elif subsribed_status == "n":
    #        new_subsribed = 0
    #    new_subsribed = subscribed
    #else:
    #    print("Invalid user ID.")
    pass


def delete_customer():
    view.print_error_message("Not implemented yet.")


def get_subscribed_emails():
    #view.print_error_message("Not implemented yet.")
    for customer in crm.customers:
        if customer.subscribed == "1":
            print(customer.email)

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
