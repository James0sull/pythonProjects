import Lens_Pizza_Data


def output(opt):
    match opt:
        case "display_menu":
            menu_display = """
            ===== Len's Pizza menu ====
            1. Pizza List
            2. Sides
            3. Drinks 
            4. Order
            5. Exit
            """
            print(menu_display)

        case "pizza list":
            pizza_plus_prices = Lens_Pizza_Data.pizza_and_prices
            result = ""
            for price, name in pizza_plus_prices:
                result += f"\t\t\t- {name.title()} pizza: €{price}\n"
            print(f"\t\t === List of Pizza's ==== \n{result}")

        # case "Receipt":


        case _:
            print("Not option to select")


# testing output
# output("display_menu")
# output("pizza list")
