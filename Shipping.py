# sal's Shipping
# Dionne 

weight = 41.5

# Ground Shipping:
if weight <= 2: # 2 lb or less
  cost_ground = weight * 1.5 + 20
elif weight <= 6: # over 2 lb but less than or equal to 6 lb
  cost_ground = weight * 3.0 + 20
elif weight <= 10: # over 6 lb but less than or equal to 10 lb
  cost_ground = weight * 4.0 + 20
else: # over 10 lb
  cost_ground = weight * 4.75 + 20

print("Ground Shipping $", cost_ground)

# Ground Shipping Premium:
cost_ground_premium = 125.00

print("Ground Shipping Premium $", cost_ground_premium)

# Drone Shipping:
if weight <= 2: # 2 lb or less
  cost_drone = weight * 4.50 
elif weight <= 6: # Over 2 lb but less than or equal to 6 lb
  cost_drone = weight * 9.0 
elif weight <= 10: # Over 6 lb but less than or equal to 10 lb
  cost_drone = weight * 12.0
else: # Over 10 lb
  cost_drone = weight * 14.25

print("drone shipping $", cost_drone)
