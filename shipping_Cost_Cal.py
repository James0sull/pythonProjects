def cost_ground(weight):
    if weight <= 2:
        cost = 1.50
    elif weight <= 6:
        cost = 3.00
    elif weight <= 10:
        cost = 4.00
    else:
        cost = 4.75
    return 20 + (cost * weight)


shipping_premium = 125.00


def drone_shipping(weight):
    if weight <= 2:
        price = 4.50
    elif weight <= 6:
        price = 9.00
    elif weight <= 10:
        price = 12.00
    else:
        price = 14.25
    return price * weight


# print(drone_shipping(4.8))
# print(cost_ground(4.8))

# Ground Shipping
weight = 8.4
if weight <= 2:
    cost = 1.50
elif weight <= 6:
    cost = 3.00
elif weight <= 10:
    cost = 4.00
else:
    cost = 4.75
ground_shipping_cost = 20 + (cost * weight)
print(f"The cost of ground shipping for a {weight} pound package is: ${ground_shipping_cost:.2f}")

# Ground Shipping Premium
premium_ground_cost = shipping_premium
print(f"The cost of premium ground shipping is: ${premium_ground_cost:.2f}")

# Drone Shipping
weight = 1.5
if weight <= 2:
    cost = 4.50
elif weight <= 6:
    cost = 9.00
elif weight <= 10:
    cost = 12.00
else:
    cost = 14.25
drone_shipping_cost = (cost * weight)
print(f"The cost of drone shipping for a {weight} pound package is: ${drone_shipping_cost:.2f}")


weight_4_8 = 4.8
cost_ground_4_8 = cost_ground(weight_4_8)
cost_drone_4_8 = drone_shipping(weight_4_8)
cost_premium = shipping_premium

if cost_ground_4_8 < cost_drone_4_8 and cost_ground_4_8 < cost_premium:
    cheapest_4_8_method = "Ground Shipping"
    cheapest_4_8_cost = cost_ground_4_8
elif cost_drone_4_8 < cost_ground_4_8 and cost_drone_4_8 < cost_premium:
    cheapest_4_8_method = "Drone Shipping"
    cheapest_4_8_cost = cost_drone_4_8
else:
    cheapest_4_8_method = "Premium Ground Shipping"
    cheapest_4_8_cost = cost_premium

print(f"\nFor a {weight_4_8} pound package:")
print(f"Ground Shipping cost: ${cost_ground_4_8:.2f}")
print(f"Drone Shipping cost: ${cost_drone_4_8:.2f}")
print(f"Premium Ground Shipping cost: ${cost_premium:.2f}")
print(f"The cheapest method is {cheapest_4_8_method} at a cost of ${cheapest_4_8_cost:.2f}")

