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

crm_data_list = data_manager.read_table_from_file(DATAFILE, separator=';')

table = crm_data_list

def modify_csv_data():
    writing_in_file = data_manager.write_table_to_file(DATAFILE, table, separator=";")

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

for customer in range(len(crm_data_list)):
    customers.append(one_customer(crm_data_list[customer][0], crm_data_list[customer][1], crm_data_list[customer][2],crm_data_list[customer][3]))

