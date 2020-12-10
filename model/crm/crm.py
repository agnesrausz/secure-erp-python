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


table = data_manager.read_table_from_file(DATAFILE, separator=';')

def modify_csv_data():
    data_manager.write_table_to_file(DATAFILE, table, separator=";")

def create_id():
    user_id = util.generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars="_+-!")
    return user_id

customers = []

class one_customer:
    def __init__(self, id, name, email, subscribed):
        self.id = id
        self.name = name
        self.email = email
        self.subscribed = subscribed

for customer in range(len(table)):
    customers.append(one_customer(table[customer][0], table[customer][1], table[customer][2],table[customer][3]))

