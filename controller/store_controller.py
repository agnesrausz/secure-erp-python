# everything you'll need is imported:
from model.store import store
from view import terminal_view


def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    options = ["Get counts of all manufacturers",
               "Get the oldest game",
               "Get cheapest game",
               "Get average games' price by a manufacturer",
               "Get age of a game by its title",
               "Find a game by a keyword",
               "Add a new record to table",
               "Update an existing record",
               "Delete an existing record from table",
               "Print the whole table",
               "Write the current table to file"]

    welcome = """
                 _______.___________.  ______   .______       _______ 
                /       |           | /  __  \  |   _  \     |   ____|
               |   (----`---|  |----`|  |  |  | |  |_)  |    |  |__   
                \   \       |  |     |  |  |  | |      /     |   __|   
            .----)   |      |  |     |  `--'  | |  |\  \----.|  |____  
            |_______/       |__|      \______/  | _| `._____||_______| 
                                                                                                                                     
    """

    table = store.get_table()
    store.check_table(table)

    choice = None

    while choice != "0":
        choice = terminal_view.get_choice_store(welcome, options)
        
        if choice == "1":
            label = "The list of manufacturers: "
            result = store.get_counts_by_manufacturers(table)
            terminal_view.print_result(result, label)

        elif choice == "2":
            label = "The oldest game is: "
            result = store.get_oldest_game(table)
            terminal_view.print_result(result, label)

        elif choice == "3":
            label = "The cheapest game is: "
            result = store.get_cheapest_game(table)
            terminal_view.print_result(result, label)

        elif choice == "4":
            manufacturer = terminal_view.get_inputs(["Manufacturer: "], "Provide a valid name of a manufacturer")
            all_manufacturers = store.get_counts_by_manufacturers(table)
            while manufacturer[0] not in all_manufacturers:
                manufacturer = terminal_view.get_inputs(["Manufacturer: "], "The manufacturer provided doesn't exist in the file, provide a valid one")
            result = store.get_average_by_manufacturer(table, manufacturer[0])
            label = "The average games' price of " + manufacturer[0] + " is: "
            terminal_view.print_result(result, label)

        elif choice == "5":
            label = "The age of a given title is (in years): "
            title = terminal_view.get_inputs(["Title: "], "Provide a valid game title")
            all_titles = []
            for game in table:
                game_title = game[1]
                all_titles.append(game_title)
            while title[0] not in all_titles:
                title = terminal_view.get_inputs(["Title: "], "No such title in the file. Provide a valid game title")
            result = store.get_age_by(title[0], table)
            terminal_view.print_result(result, label)

        elif choice == "6":
            label = "The result is: "
            keyword = terminal_view.get_inputs(["Keyword: "], "Provide a keyword to search the game by")
            result = store.get_game_by(keyword[0], table)
            terminal_view.print_result(result, label)

        elif choice == "7":
            id =  store.generate_random(table)
            record_to_add = terminal_view.get_inputs(["Title: ", "Manufacturer: ", "Price: ", "Release date: "], "Provide the properties of the game you want to add")
            record = []
            record.append(id)
            for properties in record_to_add:
                record.append(properties)
            store.create(table, record)

        elif choice == "8":
            id_ = terminal_view.get_inputs(["Game ID: "], "Provide the game ID of the record you want to update")
            record = terminal_view.get_inputs(["Title: ", "Manufacturer: ", "Price: ", "Release date: "], "Provide the properties of the game you want to be updated")
            store.update(table, id_[0], record)
        
        elif choice == "9":
            id_ = terminal_view.get_inputs(["Game ID: "], "Provide the game ID you want to delete")
            store.delete(table, id_[0])

        elif choice == "10":
            title_list = store.get_table()[0]
            terminal_view.print_table(table, title_list)
        
        elif choice == "11":
            file_to_write = terminal_view.get_inputs(["File name: "], "Provide a name of file to write the table to")
            store.write_table_to_file(file_to_write[0], table)

        elif choice == "0":
            terminal_view.print_result("", "You are going back to the main menu")

        else:
            terminal_view.print_error_message("There is no such choice.")
