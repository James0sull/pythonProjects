# pizza_functions.py

from Lens_Pizza_Data import pizza_and_prices
from Order_class import Order


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
            pizza_plus_prices = pizza_and_prices
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

def take_order():
    pizza_data = pizza_and_prices
    orders = []
    while True:
        print("Pizza List:")
        for price, name in pizza_data:
            print(f"{name}: €{price}")
        choice = input("Choose a pizza (or type 'done' to finish): ").strip().lower().title()
        if choice == 'Done':
            break

        normalized_pizza_names = [item[1].strip().lower().title() for item in pizza_data]
        if choice not in normalized_pizza_names:
            print("Sorry, that's not on the menu. Try again.")
            continue

        selected_pizza = next((item for item in pizza_data if item[1].strip().lower().title() == choice), None)
        if not selected_pizza:
            print("Error: Could not find the price for that pizza.")
            continue

        try:
            qty = int(input(f"How many {choice}s would you like? "))
        except ValueError:
            print("Invalid quantity. Try again.")
            continue

        price = selected_pizza[0]
        pizza_name = selected_pizza[1].strip().lower().title()
        order = Order(pizza_name, qty, price)
        orders.append(order)
        print(f"Added {qty} x {choice} to your order.\n")

    return orders