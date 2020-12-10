def print_menu(title, list_options):
    """Prints options in standard menu format like this:

    Main menu:
    (1) Store manager
    (2) Human resources manager
    (3) Inventory manager
    (0) Exit program

    Args:
        title (str): the title of the menu (first row)
        list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)
    """
    print(title)
    for (option_number, option_name) in enumerate(list_options[1:], start=1):
        #  We use enumerate to get the indexes (option_number) and the name of the options from the list
        #  We start enumerating from the 1. index (2nd element) so we can print out all of the options with their indexes
        print("(" + str(option_number) + ")", option_name)
    print("(0)" + list_options[0])
    # Now we print out the exit option, we don't have to mess with it in the enumeration as it will always be the first element.  


def print_message(message):
    """Prints a single message to the terminal.

    Args:
        message: str - the message
    """
    print(message)


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """
    pass


# /--------------------------------\
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \-----------------------------------/
def print_table(table):
    """Prints tabular data like above.

    Args:
        table: list of lists - the table to print out
    """
    length = 0
    lists_in_list = 0
    for i in table:
        lists_in_list += 1
        for j in i:
            if length < len(j):
                length = len(j)
    print("/" + (length*len(table[0])+2)*"-" + "\\")
    for i in table:
        for j in i:
            print("|" + j + ((length - len(j)) * " "), end="")
        print("|", end="")
        print()
        print("|" + ((length)*"-" + "|")*len(table[0]))
    print("\\" + (length*len(table[0])+2)*"-" + "/")


def get_input(label):
    """Gets single string input from the user.

    Args:
        label: str - the label before the user prompt
    """
    user_input = input(label + ":")
    return user_input


def get_inputs(labels):
    """Gets a list of string inputs from the user.

    Args:
        labels: list - the list of the labels to be displayed before each prompt
    """
    input_list = []
    i = 0
    print("Press q to quit")
    while True:
        try:
            inp = input(labels[i] + ":")
            if inp == "q":
                input_list = []
                break  # if the user presses q before every info were provided,
            else:      # the program sets the list to an empty list, then breaks out from the endless input loop
                input_list.append(inp)
                i += 1  # this generates an index error, If that occurs, we know that we got all the input we needed
        except IndexError:  # if the index error occurs, we break out from the endless input loop
            print("Thank you for the informations!")
            break
    return input_list


def print_error_message(message):
    """Prints an error message to the terminal.

    Args:
        message: str - the error message
    """
    print("Error!\n" + message)
