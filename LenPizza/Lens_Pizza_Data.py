# Len's Pizza Program
# You work at Len’s Slice, a new pizza joint in the neighborhood.
# You are going to organize some of your sales data write a python program with lists.
# Len_Pizza.py

toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

prices = [2, 6, 1, 3, 2, 7, 2]

num_two_dollar_slices = prices.count(2)
# print(f"The total number of $2 pizza's = {num_two_dollar_slices}\n")

num_pizzas = len(toppings)

# print(f"We sell  {str(num_pizzas)} different kinds of pizza!")

pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]

# print(f"The List of pizza's and the price per slice {pizza_and_prices}\n")

pizza_and_prices_sort = sorted(pizza_and_prices)
# print(f" Pizza and prices in order {pizza_and_prices_sort}\n")

cheapest_pizza = pizza_and_prices_sort[0]
# print(f"The cheapest pizza is: {cheapest_pizza}\n")

priciest_pizza = pizza_and_prices_sort[-1]
# print(f"Most priciest pizza is: {priciest_pizza}\n")

pizza_and_prices_sort.pop()
# print(f"The last pizza on the list has been is gone so here is the new list:\n {pizza_and_prices_sort}\n")

pizza_and_prices_sort.append([2.5, "peppers"])
pizza_and_prices_sort.sort()

# print(f"There is a new pizza on the sale. Here is the new list:\n {pizza_and_prices_sort}\n")

three_cheapest = pizza_and_prices_sort[:3]

# print(f"The 3 cheapest pizza's on sale are: {pizza_and_prices_sort}\n")