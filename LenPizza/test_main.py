import Lens_Pizza_Data

# test_main.py

print(f"The total number of $2 pizza's = {Lens_Pizza_Data.num_two_dollar_slices}\n")
print(f"We sell  {str(Lens_Pizza_Data.num_pizzas)} different kinds of pizza!")
print(f"The List of pizza's and the price per slice {Lens_Pizza_Data.pizza_and_prices}\n")

print(f" Pizza and prices in order {Lens_Pizza_Data.pizza_and_prices_sort}\n")

print(f"The cheapest pizza is: {Lens_Pizza_Data.cheapest_pizza}\n")

print(f"Most priciest pizza is: {Lens_Pizza_Data.priciest_pizza}\n")

print(f"The last pizza on the list has been is gone so here is the new list:\n {Lens_Pizza_Data.pizza_and_prices_sort}\n")

print(f"There is a new pizza on the sale. Here is the new list:\n {Lens_Pizza_Data.pizza_and_prices_sort}\n")

print(f"The 3 cheapest pizza's on sale are: {Lens_Pizza_Data.pizza_and_prices_sort}\n")
