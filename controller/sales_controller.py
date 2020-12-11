from model.sales import sales
from view import terminal_view
from model import data_manager


def run():

    options = ["Add a new transaction",
               "Filter transactions by the employee",
               "Filter transactions by the customer",
               "Get the sales of games by a manufacturer",
               "Get a ranking of sold items per manufacturer",
               "Get a ranking of sold items and earned money",
               "Get all the granted discounts",
               "Get the most earning employee",
               "Get the worst earning employee",
               "Get all employee sales results"]

    welcome = """
              #####     #        #####     #
             #     #   # #      #     #   # #
             #        #   #     #        #   #
              #####  #     #     #####  #     #
                   # #######          # #######
             #     # #     #    #     # #     #
              #####  #     #     #####  #     #

             #       #######    #       #######
             #       #          #       #
             #       #          #       #
             #       #####      #       #####
             #       #          #       #
             #       #          #       #
             ####### #######    ####### #######


    """

    choice = None

    while choice != "0":
        choice = terminal_view.get_choice_store(welcome, options)
        table = sales.get_table()

        if choice == "1":
            label = "Provide new record /n"
            id = sales.generate_random(table)
            id_position = 0 
            title_position = 1

            store_table = data_manager.get_table_from_file("model/store/games.csv")
            store_id_list = data_manager.get_column_from_table(store_table, id_position)
            store_titles_list = data_manager.get_column_from_table(store_table, title_position)
            store_id = terminal_view.get_input_from_list(store_id_list, store_titles_list, "Provide correct store ID, or game title ")

            hr_table = data_manager.get_table_from_file("model/hr/persons.csv")
            hr_id_list = data_manager.get_column_from_table(hr_table, id_position)
            hr_titles_list = data_manager.get_column_from_table(hr_table, title_position)
            hr_id = terminal_view.get_input_from_list(hr_id_list, hr_titles_list, "Provide correct employee ID, or name")

            crm_table = data_manager.get_table_from_file("model/crm/customers.csv")
            crm_id_list = data_manager.get_column_from_table(crm_table, id_position)
            crm_titles_list = data_manager.get_column_from_table(crm_table, title_position)
            crm_id = terminal_view.get_input_from_list(crm_id_list, crm_titles_list, "Provide correct customer ID, or name")

            qty = terminal_view.get_inputs(["Quantity: "], "Provide item quantity")
            table_updated = sales.add_transaction(table, id, store_id, hr_id, crm_id, qty[0])
            data_manager.write_table_to_file("model/sales/sales.csv", table_updated)

        elif choice == "2":
            label = "The transactions made by given employee: "
            employee_id = terminal_view.get_inputs(["Employee ID: "], "Provide the employee ID to search for his/her transactions")
            result = sales.filter_by_employee(table, employee_id[0])
            terminal_view.print_result(result, label)

        elif choice == "3":
            label = "The transactions made by given customer: "
            customer_id = terminal_view.get_inputs(["Customer ID: "], "Provide customer's ID to search for his/her transactions")
            result = sales.filter_by_customer(table, customer_id[0])
            terminal_view.print_result(result, label)

        elif choice == "4":
            label = "Number of games sold by a given manufacturer: "
            manufacturer = terminal_view.get_inputs(["Manufacturer: "], "Provide manufacturer's name")
            result = sales.filter_by_manufacturer(table, manufacturer[0])
            terminal_view.print_result(result, label)

        elif choice == "5":
            label = "Manufacturer | sold copies"
            result = sales.rank_by_manufacturer(table)
            terminal_view.print_result(result, label)

        elif choice == "6":
            raport = sales.generate_raport(table)
            raport_header = ["title", "total earnings"]
            terminal_view.print_table(raport, raport_header)
            data_manager.write_table_to_file("model/sales/raport.csv", raport)

        elif choice == "7":
            label = "All discounts granted"
            result = sales.get_discounts(table)
            terminal_view.print_result(result, label)
        
        elif choice == "8":
            label = "Most earning employee"
            result = sales.most_earned(table)
            terminal_view.print_result(result, label)

        elif choice == "9":
            label = "Min earning employee"
            result = sales.min_earned(table)
            terminal_view.print_result(result, label)

        elif choice == "10":
            label = "All employee sales results"
            result = sales.employees_earning(table)
            terminal_view.print_result(result, label)

        elif choice == "0":
            terminal_view.print_result("", "You are going back to the main menu")

        else:
            terminal_view.print_error_message("There is no such choice.")
