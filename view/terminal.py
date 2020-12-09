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
    # number 0 means the first element of the list, "Exit Program"
    # number 1 means the second element of the list, "Store Manager"
    # number 2 means the third element of the list, "Human resources manager"
    # number 3 means the fourth element of the list, "Inventory manager"
    print(

        title + ":\n"
        + "(1) " + list_options[1] + "\n"
        + "(2) " + list_options[2] + "\n"
        + "(3) " + list_options[3] + "\n"
        + "(0) " + list_options[0] + "\n"

        )


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
    pass


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
                break
            else:
                input_list.append(inp)
                i += 1  # this generates an index error, If that occurs, we know that we got all the input we needed
        except IndexError:  # if the index error occurs, we break out from the endless input loop
            print("Thank you for the informations!")
            break


def print_error_message(message):
    """Prints an error message to the terminal.

    Args:
        message: str - the error message
    """
    print("Error!\n" + message)
