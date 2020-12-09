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

#user_id = util.generate_id(11)

customers = []

class one_customer:
    def __init__(self, id, name, email, subscribed):
        self.id = id
        self.name = name
        self.email = email
        self.subscribed = subscribed

for customer in range(len(crm_data_list)):
    customers.append(one_customer(crm_data_list[customer][0], crm_data_list[customer][1], crm_data_list[customer][2],crm_data_list[customer][3]))