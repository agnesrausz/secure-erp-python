from model.crm import crm
from view import terminal as view
from model import util

def list_customers():
    print("The current list of the customers is: ")
    for customer in crm.customers:
        print("- %s" %customer.name)

def add_customer():
    import re
    new_customer = []
    valid_email = False

    #creating ID
    user_id = crm.create_id()
    new_customer.append(user_id)

    #getting new name
    name = input("Username: ")
    new_customer.append(name)

    #checking if give e-mail is in the correct format ([something]@[something].[something])
    while valid_email != True:
        email = input("E-mail: ")
        
        if re.match("\A(?P<name>[\w\-_]+)@(?P<domain>[\w\-_]+).(?P<toplevel>[\w]+)\Z",email,re.IGNORECASE):
            valid_email = True
            new_customer.append(email)
        else:
            print("Invalid e-mail adress!")

    #getting subscribed status
    subsribed_status = input("Is %s subsribed? (y/n) "%name)
    if subsribed_status == "y":
        subscribed = "1"
        new_customer.append(subscribed)
    elif subsribed_status == "n":
        subscribed = "0"
        new_customer.append(subscribed)

    #showing user ID
    print("%s's user ID is:"%name, user_id)

    #adding new customer to the existing list
    crm.table.append(new_customer)
    crm.modify_csv_data()
    


def update_customer():
    import re
    valid_email = False
    invalid_user = True
    
    while invalid_user == True:
        ask_user_id = input("Please insert the user's ID you'd like to update: ")
        for crm_data_list_first_index in range(len(crm.crm_data_list)):
            for crm_data_list_second_index in range(len(crm.crm_data_list)):
                if crm.crm_data_list[crm_data_list_first_index][crm_data_list_second_index] == ask_user_id:
                    invalid_user = False
                    new_name = input("New name: ")
                    name = new_name
                    while valid_email != True:
                        new_email = input("E-mail: ")
                        if re.match("\A(?P<name>[\w\-_]+)@(?P<domain>[\w\-_]+).(?P<toplevel>[\w]+)\Z",new_email,re.IGNORECASE):
                            valid_email = True
                            email = new_email
                        else:
                            print("Invalid e-mail adress!")
                    subsribed_status = input("Is %s subsribed? (y/n) "%name)
                    if subsribed_status == "y":
                        new_subsribed = 1
                        subscribed = new_subsribed
                    elif subsribed_status == "n":
                        new_subsribed = 0
                        subscribed = new_subsribed
        if invalid_user == True:
            print("Invalid user ID.")
                


def delete_customer():
    view.print_error_message("Not implemented yet.")


def get_subscribed_emails():
    print("E-mail adresses of the subsribed customers: ")
    for customer in crm.customers:
        if customer.subscribed == "1":
            print("- %s" %customer.email)

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
