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
    invalid_user = True
    valid_email = False
    length = len(crm.table)
    while invalid_user == True:
        ask_user_id = input("Please insert the user's ID you'd like to update: ")
        for first_index in range(length):
            for second_index in range(length):
                if ask_user_id == crm.table[first_index][second_index]:
                    invalid_user = False
                    new_name = input("New name: ")
                    while valid_email != True:
                        new_email = input("E-mail: ")
        
                        if re.match("\A(?P<name>[\w\-_]+)@(?P<domain>[\w\-_]+).(?P<toplevel>[\w]+)\Z",new_email,re.IGNORECASE):
                            valid_email = True
                        else:
                            print("Invalid e-mail adress!")
                    subsribed_status = input("Is %s subsribed? (y/n) "%new_name)
                    if subsribed_status == "y":
                            new_subsribed = "1"
                    elif subsribed_status == "n":
                            new_subsribed = "0"

                    crm.table[first_index][second_index] = ask_user_id
                    crm.table[first_index][second_index+1] = new_name
                    crm.table[first_index][second_index+2] = new_email
                    crm.table[first_index][second_index+3] = new_subsribed
                    crm.modify_csv_data()
        if invalid_user == True:
            print("Invalid id")
          

def delete_customer():

    invalid_user = True
    #delete_done = False
    delete_user_id = input("Please give the ID of the user you'd like to delete: ")
    for first_index in range(1):
        for second_index in range(1):
            if delete_user_id == crm.table[first_index][second_index]:
                invalid_user = False
                crm.table.pop(first_index)
                crm.modify_csv_data()
        if invalid_user == True:
            print("Invalid id")

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
