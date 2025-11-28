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
    if (not customer.get("id") or
            not customer.get("name") or
            not customer.get("email") or
            not customer.get("subscribed")):
        raise KeyError("Customer dictionary is missing required fields.")
    table_row = [customer["id"], customer["name"], customer["email"], customer["subscribed"]]
    table.append(table_row)
    data_manager.write_table_to_file(DATAFILE, table)
    return customer["id"]
