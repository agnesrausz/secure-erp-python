from model import util
from model.hr import hr
from view import terminal as view


# TODO:
#     (5) Return the names of the oldest and the youngest employees as a tuple.
#     (6) Return the average age of employees.
#     (7) Return the names of employees having birthdays within the two weeks starting from the given date.
#     (8) Return the number of employees with at least the given clearance level.
#     (9) Return the number of employees per department in a dictionary (like {'dep1': 5, 'dep2': 11}).
def list_employees():
    """ Display a list of employees with their details. """
    employees = hr.get_employees()
    headers = hr.HEADERS
    table = [headers]
    for employee in employees:
        row = []
        for header in headers:
            row.append(employee[header])
        table.append(row)
    view.print_table(table)
    view.wait_for_enter()


def add_employee():
    """Add a new employee to the HR system."""
    employee = {
        "Name": "",
        "Date of birth": "",
        "Department": "",
        "Clearance": ""
    }

    is_valid_name = False
    while not is_valid_name:
        view.clear()
        view.print_message("Adding a new employee")
        name = view.get_input("Name")
        if not name:
            view.print_error_message("Name cannot be empty. Please enter a valid name.")
        elif any((not char.isalnum() and char not in [" ", "-", "."]) for char in name):
            view.print_error_message("Name contains invalid characters. Please enter a valid name.")
        else:
            is_valid_name = True
            employee['Name'] = name

    is_valid_date = False
    while not is_valid_date:
        view.clear()
        view.print_message("Adding a new employee")
        view.print_message(f"Name: {employee['Name']}")
        date_str = view.get_input("Date of birth (YYYY-MM-DD)")

        if not date_str:
            view.print_error_message("Date of birth cannot be empty. Please enter a valid date.")
        else:
            try:
                parsed_date = util.parse_date_to_iso_format(date_str)
                is_valid_date = True
                employee["Date of birth"] = parsed_date
            except ValueError:
                view.print_error_message("Invalid date. Please enter date in YYYY-MM-DD format.")

    is_valid_department = False
    while not is_valid_department:
        view.clear()
        view.print_message("Adding a new employee")
        department = view.get_input("Department").capitalize()
        if not department:
            view.print_error_message("Department cannot be empty. Please enter a valid department.")
        elif any((not char.isalnum() and char not in [" ", "-"]) for char in department):
            view.print_error_message("Department contains invalid characters. Please enter a valid department.")
        else:
            is_valid_department = True
            employee['Department'] = department

    is_valid_clearance = False
    while not is_valid_clearance:
        view.clear()
        view.print_message("Adding a new employee")
        clearance = view.get_input("Clearance").capitalize()
        if not clearance:
            view.print_error_message("Clearance cannot be empty. Please enter a valid value.")
        elif any(not char.isnumeric() for char in clearance):
            view.print_error_message("Clearance must be a number. Please enter a valid value.")
        else:
            is_valid_clearance = True
            employee['Clearance'] = clearance

    try:
        hr.add_employee(employee)
        view.clear()
        view.print_message("Adding a new employee")
        view.print_message(f"Name: {employee['Name']}")
        view.print_message(f"Date of birth: {employee['Date of birth']}")
        view.print_message(f"Department: {employee['Department']}")
        view.print_message(f"Clearance: {employee['Clearance']}")
        view.print_message("New employee added.")
    except KeyError as err:
        view.print_error_message(err)
    view.wait_for_enter()


def update_employee():
    """Update an existing employee's details."""
    employee = {
        "Id": "",
        "Name": "",
        "Date of birth": "",
        "Department": "",
        "Clearance": ""
    }

    is_valid_id = False
    while not is_valid_id:
        view.clear()
        view.print_message("Updating an employee")
        employee_id = view.get_input("Employee ID")
        if not employee_id:
            view.print_error_message("Customer ID cannot be empty. Please enter a valid ID.")
        elif not hr.is_id_exist(employee_id):
            view.print_error_message("Customer ID does not exist. Please enter a valid ID.")
        else:
            is_valid_id = True
            employee = hr.get_employee_by_id(employee_id)

    is_valid_name = False
    while not is_valid_name:
        view.clear()
        view.print_message("Updating an employee")
        name = view.get_input("Name")
        if not name:
            # Keep existing name if input is empty
            is_valid_name = True
        elif any((not char.isalnum() and char not in [" ", "-", "."]) for char in name):
            view.print_error_message("Name contains invalid characters. Please enter a valid name.")
        else:
            is_valid_name = True
            employee['Name'] = name

    is_valid_date = False
    while not is_valid_date:
        view.clear()
        view.print_message("Updating an employee")
        view.print_message(f"Name: {employee['Name']}")
        date_str = view.get_input("Date of birth (YYYY-MM-DD)")
        if not date_str:
            # Keep existing date if input is empty
            is_valid_date = True
        else:
            try:
                parsed_date = util.parse_date_to_iso_format(date_str)
                is_valid_date = True
                employee["Date of birth"] = parsed_date
            except ValueError:
                view.print_error_message("Invalid date. Please enter date in YYYY-MM-DD format.")

    is_valid_department = False
    while not is_valid_department:
        view.clear()
        view.print_message("Updating an employee")
        department = view.get_input("Department").capitalize()
        if not department:
            # Keep existing department if input is empty
            is_valid_department = True
        elif any((not char.isalnum() and char not in [" ", "-"]) for char in department):
            view.print_error_message("Department contains invalid characters. Please enter a valid department.")
        else:
            is_valid_department = True
            employee['Department'] = department

    is_valid_clearance = False
    while not is_valid_clearance:
        view.clear()
        view.print_message("Updating an employee")
        clearance = view.get_input("Clearance").capitalize()
        if not clearance:
            # Keep existing clearance if input is empty
            is_valid_clearance = True
        elif any(not char.isnumeric() for char in clearance):
            view.print_error_message("Clearance must be a number. Please enter a valid value.")
        else:
            is_valid_clearance = True
            employee['Clearance'] = clearance

    try:
        hr.update_employee(employee)
        view.clear()
        view.print_message("Updating an employee")
        view.print_message(f"Name: {employee['Name']}")
        view.print_message(f"Date of birth: {employee['Date of birth']}")
        view.print_message(f"Department: {employee['Department']}")
        view.print_message(f"Clearance: {employee['Clearance']}")
        view.print_message("Employee updated.")
    except KeyError as err:
        view.print_error_message(err)
    view.wait_for_enter()


def delete_employee():
    """Delete an employee from the HR system."""
    employee_id = ""
    is_valid_id = False
    while not is_valid_id:
        view.clear()
        view.print_message("Removing an employee")
        employee_id = view.get_input("Employee ID")
        if not employee_id:
            view.print_error_message("Employee ID cannot be empty. Please enter a valid ID.")
        elif not hr.is_id_exist(employee_id):
            view.print_error_message("Employee ID does not exist. Please enter a valid ID.")
        else:
            is_valid_id = True

    try:
        hr.delete_employee(employee_id)
        view.clear()
        view.print_message("Removing an employee")
        view.print_message(f"Employee with ID {employee_id} has been removed.")
    except KeyError as err:
        view.print_error_message(err)
    view.wait_for_enter()


def get_oldest_and_youngest():
    """Display the names of the oldest and youngest employees."""
    employees = hr.get_employees()
    oldest_employee = None
    oldest_birthdate = None
    youngest_employee = None
    youngest_birthdate = None

    for employee in employees:
        birthdate = util.parse_date_to_iso_format(employee['Date of birth'])
        if oldest_birthdate is None or birthdate < oldest_birthdate:
            oldest_birthdate = birthdate
            oldest_employee = employee['Name']
        if youngest_birthdate is None or birthdate > youngest_birthdate:
            youngest_birthdate = birthdate
            youngest_employee = employee['Name']

    view.clear()
    view.print_message("Oldest and youngest employees")
    view.print_message(f"Oldest employee: {oldest_employee}")
    view.print_message(f"Youngest employee: {youngest_employee}")
    view.wait_for_enter()
    return oldest_employee, youngest_employee


def get_average_age():
    """Display the average age of employees."""
    employees = hr.get_employees()
    total_age = 0
    current_date = util.get_current_date_iso_format()
    current_year, current_month, current_day = current_date.split("-")
    current_year = int(current_year)
    current_month = int(current_month)
    current_day = int(current_day)

    for employee in employees:
        birth_year, birth_month, birth_day = employee["Date of birth"].split("-")
        birth_year = int(birth_year)
        birth_month = int(birth_month)
        birth_day = int(birth_day)

        age = current_year - birth_year
        if (current_month, current_day) < (birth_month, birth_day):
            age -= 1

        total_age += age

    average_age = total_age // len(employees) if employees else 0

    view.clear()
    view.print_message("Employees average age")
    view.print_message(f"Average age: {average_age} years")
    view.wait_for_enter()
    return average_age


def next_birthdays():
    """Display names of employees with birthdays in the next two weeks."""
    employees = hr.get_employees()
    current_date = util.get_current_date()
    end_date = util.get_delayed_date(current_date, 14)

    upcoming = []
    for employee in employees:
        birthdate = util.parse_date_to_date(employee["Date of birth"])
        birthday_this_year = util.get_birthday_in_year(birthdate, current_date.year)

        if current_date <= birthday_this_year <= end_date:
            upcoming.append(employee["Name"])

    view.clear()
    view.print_message("Employees with birthdays in the next two weeks")
    if upcoming:
        for name in upcoming:
            view.print_message(name)
    else:
        view.print_message("No upcoming birthdays.")

    view.wait_for_enter()
    return upcoming


def count_employees_with_clearance():
    """Display the number of employees with at least the given clearance level."""
    employees = hr.get_employees()

    is_valid_clearance = False
    min_clearance = 0

    while not is_valid_clearance:
        view.clear()
        view.print_message("Count employees with clearance level")
        clearance = view.get_input("Minimum clearance level")

        if not clearance:
            view.print_error_message("Clearance cannot be empty. Please enter a valid number.")
        elif not clearance.isdigit():
            view.print_error_message("Clearance must be a number. Please enter a valid value.")
        else:
            is_valid_clearance = True
            min_clearance = int(clearance)

    count = 0
    for employee in employees:
        if int(employee["Clearance"]) >= min_clearance:
            count += 1

    view.clear()
    view.print_message("Count employees with clearance level")
    view.print_message(f"Employees with clearance level {min_clearance}: {count}")
    view.wait_for_enter()
    return count


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
