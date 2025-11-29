""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""

from model import data_manager, util


DATAFILE = "model/crm/crm.csv"
HEADERS = ["id", "name", "email", "subscribed"]


def add_customer(customer):
    table = data_manager.read_table_from_file(DATAFILE)
    customer["id"] = util.generate_id()
    for key in HEADERS:
        if key not in customer:
            raise KeyError(f"Customer dictionary is missing required field: {key}")
        if customer[key] == "":
            raise KeyError(f"Customer field '{key}' must not be empty.")
    table_row = []
    for key in HEADERS:
        table_row.append(customer[key])
    table.append(table_row)
    data_manager.write_table_to_file(DATAFILE, table)
    return customer["id"]


def get_customers():
    table = data_manager.read_table_from_file(DATAFILE)
    customers = []
    for row in table:
        customer = {}
        for i in range(len(HEADERS)):
            customer[HEADERS[i]] = row[i]
        customers.append(customer)
    return customers
