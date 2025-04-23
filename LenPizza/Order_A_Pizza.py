import Lens_Pizza_Data
import The_pizza_fuct

pizza = Lens_Pizza_Data.pizza_and_prices
print_menu = The_pizza_fuct.output("pizza list")


class Order:

    def __init__(self, item, qty, price):
        self.item = item
        self.qty = qty
        self.price = price
        self.total = self.qty * self.price


def take_order():
    orders = []
    while True:
        print_menu
        choice = input("Choose a pizza (or type 'done' to finish): ").title()
        if choice == 'Done':
            break
        if choice not in pizza:
            print("Sorry, that's not on the menu. Try again.")
            continue

        try:
            qty = int(input(f"How many {choice}s would you like? "))
        except ValueError:
            print("Invalid quantity. Try again.")
            continue

        price = pizza[choice]
        order = Order(choice, qty, price)
        orders.append(order)
        print(f"Added {qty} x {choice} to your order.\n")

    return orders

