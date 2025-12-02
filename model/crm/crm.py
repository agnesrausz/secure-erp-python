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
    for row in range(len(table)):
        customer = {}
        for col in range(len(HEADERS)):
            customer[HEADERS[col]] = table[row][col]
        customers.append(customer)
    return customers


def is_id_exist(customer_id):
    table = data_manager.read_table_from_file(DATAFILE)
    for row in table:
        if row[0] == customer_id:
            return True
    return False


def update_customer(customer):
    table = data_manager.read_table_from_file(DATAFILE)
    for row in range(len(table)):
        if table[row][0] == customer["id"]:
            for col in range(len(HEADERS)):
                table[row][col] = customer[HEADERS[col]]
            data_manager.write_table_to_file(DATAFILE, table)
            return
    raise ValueError(f"Customer with id {customer['id']} not found.")


def get_customer_by_id(customer_id):
    table = data_manager.read_table_from_file(DATAFILE)
    for row in table:
        if row[0] == customer_id:
            customer = {}
            for i in range(len(HEADERS)):
                customer[HEADERS[i]] = row[i]
            return customer
    raise ValueError(f"Customer with id {customer_id} not found.")


def delete_customer_by_id(customer_id):
    table = data_manager.read_table_from_file(DATAFILE)
    for row in range(len(table)):
        if table[row][0] == customer_id:
            table.pop(row)
            data_manager.write_table_to_file(DATAFILE, table)
            return
    raise ValueError(f"Customer with id {customer_id} not found.")

