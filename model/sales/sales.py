""" Sales module

Data table structure:
    - id (string)
    - customer id (string)
    - product (string)
    - price (float)
    - transaction date (string): in ISO 8601 format (like 1989-03-21)
"""

from model import data_manager, util

DATAFILE = "model/sales/sales.csv"
HEADERS = ["id", "customer", "product", "price", "date"]


def add_transaction(transaction):
    table = data_manager.read_table_from_file(DATAFILE)
    transaction["id"] = util.generate_id()
    for key in HEADERS:
        if key not in transaction:
            raise KeyError(f"Transaction dictionary is missing required field: {key}")
        if transaction[key] == "":
            raise KeyError(f"Transaction field '{key}' must not be empty.")
    table_row = []
    for key in HEADERS:
        table_row.append(transaction[key])
    table.append(table_row)
    data_manager.write_table_to_file(DATAFILE, table)
    return transaction["id"]


def get_transactions():
    table = data_manager.read_table_from_file(DATAFILE)
    transactions = []
    for row in range(len(table)):
        transaction = {}
        for col in range(len(HEADERS)):
            transaction[HEADERS[col]] = table[row][col]
        transactions.append(transaction)
    return transactions


def get_transaction_by_id(transaction_id):
    table = data_manager.read_table_from_file(DATAFILE)
    for row in range(len(table)):
        if table[row][0] == transaction_id:
            transaction = {}
            for col in range(len(HEADERS)):
                transaction[HEADERS[col]] = table[row][col]
            return transaction
    raise ValueError(f"Transaction with id {transaction_id} not found.")


def update_transaction(transaction):
    table = data_manager.read_table_from_file(DATAFILE)
    for row in range(len(table)):
        if table[row][0] == transaction["id"]:
            for col in range(len(HEADERS)):
                table[row][col] = transaction[HEADERS[col]]
            data_manager.write_table_to_file(DATAFILE, table)
            return
    raise ValueError(f"Transaction with id {transaction['id']} not found.")


def delete_transaction(transaction_id):
    table = data_manager.read_table_from_file(DATAFILE)
    for row in range(len(table)):
        if table[row][0] == transaction_id:
            table.pop(row)
            data_manager.write_table_to_file(DATAFILE, table)
            return
    raise ValueError(f"Transaction with id {transaction_id} not found.")


def is_id_exist(transaction_id):
    table = data_manager.read_table_from_file(DATAFILE)
    for row in table:
        if row[0] == transaction_id:
            return True
    return False
