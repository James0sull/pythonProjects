# Pizza_main.py
from pizza_functions import take_order

if __name__ == "__main__":
    order_items = take_order()
    print("\n--- Your Order ---")
    total = 0
    for item in order_items:
        print(f"{item.qty} x {item.item}: €{item.total}")
        total += item.total
    print(f"\nTotal: €{total}")
