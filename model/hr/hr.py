""" Human resources (HR) module

Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""

from model import data_manager, util

DATAFILE = "model/hr/hr.csv"
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]


def add_employee(employee):
    table = data_manager.read_table_from_file(DATAFILE)
    employee["Id"] = util.generate_id()
    for key in HEADERS:
        if key not in employee:
            raise KeyError(f"Employee dictionary is missing required field: {key}")
        if employee[key] == "":
            raise KeyError(f"Employee field '{key}' must not be empty.")
    table_row = []
    for key in HEADERS:
        table_row.append(employee[key])
    table.append(table_row)
    data_manager.write_table_to_file(DATAFILE, table)
    return employee["Id"]


def get_employees():
    table = data_manager.read_table_from_file(DATAFILE)
    employees = []
    for row in range(len(table)):
        employee = {}
        for col in range(len(HEADERS)):
            employee[HEADERS[col]] = table[row][col]
        employees.append(employee)
    return employees


def get_employee_by_id(employee_id):
    table = data_manager.read_table_from_file(DATAFILE)
    for row in range(len(table)):
        if table[row][0] == employee_id:
            employee = {}
            for col in range(len(HEADERS)):
                employee[HEADERS[col]] = table[row][col]
            return employee
    raise ValueError(f"Employee with id {employee_id} not found.")


def update_employee(employee):
    table = data_manager.read_table_from_file(DATAFILE)
    for row in range(len(table)):
        if table[row][0] == employee["Id"]:
            for col in range(len(HEADERS)):
                table[row][col] = employee[HEADERS[col]]
            data_manager.write_table_to_file(DATAFILE, table)
            return
    raise ValueError(f"Employee with id {employee['Id']} not found.")


def delete_employee(employee_id):
    table = data_manager.read_table_from_file(DATAFILE)
    for row in range(len(table)):
        if table[row][0] == employee_id:
            table.pop(row)
            data_manager.write_table_to_file(DATAFILE, table)
            return
    raise ValueError(f"Employee with id {employee_id} not found.")


def is_id_exist(employee_id):
    table = data_manager.read_table_from_file(DATAFILE)
    for row in table:
        if row[0] == employee_id:
            return True
    return False