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

employees = data_manager.read_table_from_file(DATAFILE, separator=';')

def write(Employees):
    # Employees convert to 2D list
    table = 
    write_table_to_file(DATAFILE, table, separator=';')


class Employee:
    def __init__(self, id, name, birth_date, department, clearance_lvl):
        self.id = id
        self.name = name
        self.birth_date = birth_date
        self.department = department
        self.clearance_lvl = clearance_lvl


Employees = []

for employee in range(len(employees)):
    # commnet not tested
    # datas = []
    # for employee_data in range(len(employees[employee])):
    #     datas.append(employees[employee][employee_data])
    # Employees.append(Employee(datas)
    Employees.append(Employee(
        employees[employee][0], 
        employees[employee][1], 
        employees[employee][2], 
        employees[employee][3], 
        employees[employee][4]))

id = util.generate_id()