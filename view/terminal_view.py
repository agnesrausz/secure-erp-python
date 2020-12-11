""" Terminal view module """
from os import system

# colors
RESET = "\033[0;0m"
BOLD = "\033[;1m"
REVERSE = "\033[;7m"
RED = '\033[31m'
GREEN = '\033[32m'
ORANGE = '\033[33m'
BLUE = '\033[34m'
PURPLE = '\033[35m'
CYAN = '\033[36m'
LIGHTGRAY = '\033[37m'
DARKGRAY = '\033[90m'
LIGHTRED = '\033[91m'
LIGHTGREEN = '\033[92m'
YELLOW = '\033[93m'
LIGHTBLUE = '\033[94m'
PINK = '\033[95m'
LIGHTCYAN = '\033[96m'


def clear():
    _ = system('clear')


def print_table(table, title_list):
    """
    Prints table with data.

    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
       \\-----------------------------------/

    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    row_width = []
    for width in title_list:
        row_width.append(len(width))
    for line in range(0, len(table)):
        for index in range(0, len(table[line])):
            if len(table[line][index]) > row_width[index]:
                row_width[index] = len(table[line][index])

    table_lenght = 0
    for index in range(0, len(row_width)):
        row_width[index] += 2
        table_lenght += row_width[index]

    print(GREEN + "/" + "-" * (table_lenght+len(title_list)-1) + "\\" + RESET)

    for i in range(0, len(title_list)):
        temp = round((row_width[i] - len(title_list[i]))/2)
        print(GREEN + "|" + " " * temp + BOLD + title_list[i], end='')
        print(GREEN + " " * (row_width[i] - (temp + len(title_list[i]))), end='')
    print("|" + RESET)

    for line in range(0, len(table)):
        for width in row_width:
            print(GREEN + "|" + "-" * width, end='')
        print("|" + RESET)
        for index in range(0, len(table[line])):
            temp = round((row_width[index] - len(table[line][index]))/2)
            print(GREEN + "|" + " " * temp + BLUE + table[line][index], end='')
            print(GREEN + " " * (row_width[index]-temp-len(table[line][index])), end='')
        print("|" + RESET)

    print(GREEN + "\\" + "-" * (table_lenght+len(title_list)-1) + "/" + RESET)

    input(REVERSE + "Press enter to continue" + RESET)
    clear()


def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    if isinstance(result, list):
        print(LIGHTGREEN + label + '\n' + RESET)
        for element in result:
            element = str(element)
            for sign in element:
                if sign == ";":
                    sign = ' :  '
                print(YELLOW + str(sign) + RESET, end='')
            print('')
    elif isinstance(result, dict):
        first_width = 0
        secend_width = 0
        for key in result:
            key = str(key)
            result[key] = str(result[key])
            if first_width < len(key):
                first_width = len(key)
            if secend_width < len(result[key]):
                secend_width = len(result[key])
        first_width += 2
        secend_width += 1
        print('\n' + label + '\n'*2)
        for key in result:
            key = str(key)
            result[key] = str(result[key])
            temp = round((first_width-len(key))/2)
            print('|' + '-' * (first_width + secend_width + 2) + '|')
            print('|' + ' ' * temp + key + ' '*(first_width - temp - len(key)), end='')
            print('| ' + result[key] + ' ' * (secend_width - len(result[key])) + '|')
        print('|' + '-' * (first_width + secend_width + 2) + '|')

    else:
        print(LIGHTGREEN + label + '\n'*2 + YELLOW + str(result) + RESET + '\n'*2)
    input(REVERSE + "Press enter to continue" + RESET)
    clear()


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    order_number = 1
    print(RED + '\n'*2 + title + RESET)
    for option in list_options:
        print(GREEN + "     (" + str(order_number) + ") ", option + RESET)
        order_number += 1
    print(GREEN + "     (0) ", exit_message + RESET)


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    inputs = []
    print(CYAN + title + RESET)
    for label in list_labels:
        user_input = input(label)
        inputs.append(user_input)
    return inputs


def get_choice(options):
    print_menu("Main menu", options, "Exit program")
    inputs = get_inputs([CYAN + "Please enter a number: " + RESET], "")
    return inputs[0]


def get_choice_store(welcome, options):
    print_menu(welcome, options, "Go back to the main menu")
    inputs = get_inputs([BLUE + "Please choose your function: " + RESET], "")
    return inputs[0]


def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    print(RED + "Error: " + message + RESET)


def get_input_from_list(basic_list, alternative_list, message):
    """ Ask for input as long as user will not provide input from list

    Args:
    list - list to compare against (id)
    list - list to compare against (name)
    message - string to print while asking for input

    Return:
    str - validated input  """

    input_value = ""

    combined_list = basic_list + alternative_list

    while input_value not in combined_list:
        input_value = get_inputs(["Value: "], message)[0]

    if input_value in alternative_list:
        for index in range(len(basic_list)):
            if input_value == alternative_list[index]:
                input_value = basic_list[index]

    return input_value
