def ground_shipping_cost(weight):
    if weight <= 2:
      return weight * 1.50 + 20.00
    elif weight > 2 and weight <= 6:
      return weight * 3.00 + 20.00
    elif weight > 6 and weight <= 10:
      return weight * 4.00 + 20.00
    elif weight > 10:
      return weight * 4.75 + 20.00

premium_shipping_cost = 125.00

def drone_shipping_cost(weight):
    if weight <= 2:
      return weight * 4.50 + 0.00
    elif weight > 2 and weight <= 6:
      return weight * 9.00 + 0.00
    elif weight > 6 and weight <= 10:
      return weight * 12.00 + 0.00
    elif weight > 10:
      return weight * 14.25 + 0.00

def cheapest_shipping(weight):
  cost = ""
  drone = drone_shipping_cost(weight)
  ground = ground_shipping_cost(weight)
  
  if ground < drone:
    cost = "You should ship using ground shipping, it will cost $" + str(ground)
  else:
    cost = "You should ship using drone shipping, it will cost $" + str(drone)
    
  return cost

print(cheapest_shipping(17))
print(cheapest_shipping(1.5))
print(cheapest_shipping(8.4))
  

