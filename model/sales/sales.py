""" Sales module """

# modules import go here:
import random

from model import data_manager
from model.store import store
from model.hr import hr
from model.crm import crm

# global variables go here:

CUSTOMER_ID = 2
PRODUCT_ID = 3
NUMBER_OF_ITEMS = 4

STORE_PRODUCT_ID = 0
STORE_MANUFACTURER = 2


# sales.csv: 'id, employee_id, customer_id, product_id, number_of_items'


def get_table():
    file = "model/sales/sales.csv"
    table = data_manager.get_table_from_file(file)
    return table


def generate_random(table):

    id_list = []
    generated = ""
    for game in table:
        id = game[0]
        id_list.append(id)

    expected_length = 8
    while generated in id_list or len(generated) != expected_length:
        quantity = 2
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        characters = '!@#$%^&*()_+=-{}[]|\:"<>,.?/'
        random_letters = [random.choice(alphabet) for i in range(quantity)] + [random.choice(alphabet).upper() for i in range(quantity)]
        random_characters = [random.choice(characters) for i in range(quantity)]
        random_numbers = [str(random.randint(0, 9)) for i in range(quantity)]
        generated_list = [letter for letter in random_letters] + [character for character in random_characters] + [digit for digit in random_numbers]
        random.shuffle(generated_list)
        generated = "".join(generated_list)

    return generated


def add_transaction(table, id, store_id, hr_id, crm_id, quantity):

    record = [id, store_id, hr_id, crm_id, quantity]
    table.append(record)

    return table


def filter_by_employee(table, employee_id):

    operations = []
    employee_id_index = 1
    for record in table:
        id = record[employee_id_index]
        if id == employee_id:
            operations.append(record)
    return operations


def filter_by_customer(table, customer):

    transactions = []
    for record in table:
        if record[CUSTOMER_ID] == customer:
            transactions.append(record)
    return transactions


def filter_by_manufacturer(table, manufacturer):


    store_table = store.get_table()

    store_id_list = []
    for record in store_table:
        if record[STORE_MANUFACTURER] == manufacturer:
            store_id_list.append(record[STORE_PRODUCT_ID])

    sales = 0
    for record in table:
        if record[PRODUCT_ID] in store_id_list:
            sales += int(record[NUMBER_OF_ITEMS])

    return sales


def employees_earning(table):
   

    product_index = 1
    employee_id_index = 2
    amount_sold_index = 4

    person_id_index = 0
    person_name_index = 1

    game_index = 0
    price_index = 3

    store_table = store.get_table()
    store.check_table(store_table)
    hr_table = hr.get_table('model/hr/persons.csv')
    money_earned = {}
    for person in hr_table:
        person_id = person[person_id_index]
        person_name = person[person_name_index]
        money_earned[person_name] = 0
        for record in table:
            product_id = record[product_index]
            employee_id = record[employee_id_index]
            amount_sold = int(record[amount_sold_index])
            if person_id == employee_id:
                for game in store_table:
                    game_id = game[game_index]
                    if game_id == product_id:
                        game_price = int(game[price_index])
                        money_earned[person_name] += int(amount_sold * game_price)
    return money_earned


def most_earned(table):

    money_earned = employees_earning(table)
    temp = 0
    for employee in money_earned:
        if money_earned[employee] > temp:
            temp = money_earned[employee]
            most_earned_employee = str(employee) + ":" + str(money_earned[employee])
    return most_earned_employee


def min_earned(table):

    money_earned = employees_earning(table)
    temp = 0
    min_earned_employee = [0]
    for employee in money_earned:
        if temp == 0:
            temp = money_earned[employee]
        if money_earned[employee] <= temp:
            temp = money_earned[employee]
            if money_earned[employee] > 0:
                min_earned_employee[0] = (str(employee) + ": " + str(money_earned[employee]))
            elif money_earned[employee] == 0:
                min_earned_employee.append(str(employee) + ": " + str(money_earned[employee]))
    if len(min_earned_employee) > 1:
        min_earned_employee.pop(0)
    return min_earned_employee


def rank_by_manufacturer(table):

    manufacturers_counts = {}
    product_id_index = 3
    amount_sold_index = 4
    id_index = 0
    manufacturer_index = 2

    store_table = store.get_table()
    store.check_table(store_table)

    for record in table:
        product_id = record[product_id_index]
        amount_sold = record[amount_sold_index]
        for game in store_table:
            game_id = game[id_index]
            manufacturer = game[manufacturer_index]
            if product_id == game_id:
                if manufacturer in manufacturers_counts:
                    manufacturers_counts[manufacturer] += int(amount_sold)
                else:
                    manufacturers_counts[manufacturer] = int(amount_sold)

    return manufacturers_counts


def get_sold_copies(table, store_id):


    store_id_position = 1
    quantity_position = 4
    sold_copies = 0

    for record in table:
        if str(record[store_id_position]) == str(store_id):
            sold_copies = sold_copies + int(record[quantity_position])

    return sold_copies


def generate_raport(table):

    item_table = store.get_table()
    item_table = store.check_table(item_table)
    raport = []

    id_position = 0
    title_position = 1
    price_position = 3
    earnings = 0

    for item in item_table:
        price = item[price_position]
        sold_copies = get_sold_copies(table, item[id_position])
        if price and sold_copies:
            earnings = int(price) * int(sold_copies)
            raport_row = [item[title_position], str(earnings)]
            raport.append(raport_row)

    return raport


def get_discounts(table):


    discounts_money_spent = {}
    discount_levels = [100, 1000, 5000]
    discount_percents = ["2%", "5%", "10%"]

    customer_id_index = 2
    amount_sold_index = 4
    id_index = 0
    product_id_index = 3
    name_index = 1
    price_index = 3

    store_table = store.get_table()
    store.check_table(store_table)

    crm_table = crm.get_table('model/crm/customers.csv')

    for record in table:
        product_id = record[product_id_index]
        amount_sold = record[amount_sold_index]
        customer_id = record[customer_id_index]

        for customer in crm_table:
            customer_name = customer[name_index]
            client_id = customer[id_index]

            if customer_id == client_id:

                for game in store_table:
                    game_id = game[id_index]
                    price = game[price_index]
                    if product_id == game_id:
                        money_spent = int(price) * int(amount_sold)

                        if customer_name in discounts_money_spent:
                            discounts_money_spent[customer_name] += int(money_spent)
                        else:
                            discounts_money_spent[customer_name] = int(money_spent)

    discounts = {}

    for customer_name in discounts_money_spent:
        money_spent = discounts_money_spent[customer_name]
        if money_spent >= discount_levels[0] and money_spent < discount_levels[1]:
            discount = discount_percents[0]
        elif money_spent >= discount_levels[1] and money_spent < discount_levels[2]:
            discount = discount_percents[1]
        elif money_spent >= discount_levels[2]:
            discount = discount_percents[2]
        else:
            discount = "0%"

        discounts[customer_name] = discount

    return discounts
