from model.hr import hr
from view import terminal as view
from datetime import date, datetime, timedelta


def list_employees():
    for Employee in hr.Employees:
        print(Employee.name)


def add_employee():
    view.print_error_message("Not implemented yet.")


def update_employee():
    view.print_error_message("Not implemented yet.")


def delete_employee():
    view.print_error_message("Not implemented yet.")


def get_oldest_and_youngest():
    birth_dates = []
    oldest_and_youngest = []
    for Employee in hr.Employees:
        birth_dates.append(Employee.birth_date)
    for Employee in hr.Employees:
        if Employee.birth_date == min(birth_dates):
            oldest_and_youngest.append(Employee.name)
        elif Employee.birth_date == max(birth_dates):
            oldest_and_youngest.append(Employee.name)
    print(tuple(oldest_and_youngest))  # ??
    return tuple(oldest_and_youngest)


def get_average_age():
    today = date.today()
    ages = []
    for Employee in hr.Employees:
        birth_date = datetime.strptime(Employee.birth_date, '%Y-%m-%d')
        age = today.year - birth_date.year
        ages.append(age)
    print(int(sum(ages)/len(ages)))  # ??
    return (int(sum(ages)/len(ages)))


def next_birthdays():
    today = date.today()
    given_date = input("Add a date! YYYY-MM-DD or today: ")
    if given_date == "today":
        given_date = today
    else:
        given_date = datetime.strptime(given_date, '%Y-%m-%d')
    two_weeks_later = given_date + timedelta(days=14)
    next_birthdays_names = []
    for Employee in hr.Employees:
        birth_date = datetime.strptime(Employee.birth_date, '%Y-%m-%d')
        if (given_date.month, given_date.day) < (birth_date.month, birth_date.day) and (two_weeks_later.month, two_weeks_later.day) > (birth_date.month, birth_date.day):
            next_birthdays_names.append(Employee.name)
    print(next_birthdays_names)  # ??
    return(next_birthdays_names)


def count_employees_with_clearance():
    clearance_level = int(input("Add clearence level: "))
    clearance_names = []
    for Employee in hr.Employees:
        if int(Employee.clearance_lvl) <= clearance_level:
            clearance_names.append(Employee.name)
    print(clearance_names)  # ??
    return clearance_names


def count_employees_per_department():
    view.print_error_message("Not implemented yet.")


def run_operation(option):
    if option == 1:
        list_employees()
    elif option == 2:
        add_employee()
    elif option == 3:
        update_employee()
    elif option == 4:
        delete_employee()
    elif option == 5:
        get_oldest_and_youngest()
    elif option == 6:
        get_average_age()
    elif option == 7:
        next_birthdays()
    elif option == 8:
        count_employees_with_clearance()
    elif option == 9:
        count_employees_per_department()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List employees",
               "Add new employee",
               "Update employee",
               "Remove employee",
               "Oldest and youngest employees",
               "Employees average age",
               "Employees with birthdays in the next two weeks",
               "Employees with clearance level",
               "Employee numbers by department"]
    view.print_menu("Human resources", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
