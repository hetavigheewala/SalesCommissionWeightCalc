#1
# Asks for inputting sales and commission rate
sales_amount = float(input("Enter the sales amount: $"))
commission_rate = float(input("Enter the commission rate (as a percentage): "))

# Calculate commission earned
commission_earned = sales_amount * (commission_rate / 100)

# Format the commission earned to 2 decimal places
commission_earned = "{:.2f}".format(commission_earned)

# Print the commission earned for the month
print("Commission earned for the month: $" + str(commission_earned))


#2
# Asks for inputting weight in pounds and ounces, and price per pound
weight_pounds = int(input("Enter the weight in pounds: "))
weight_ounces = int(input("Enter the weight in ounces: "))
price_per_pound = float(input("Enter the price per pound: $"))

# Convert ounces to pounds
weight_in_pounds = weight_pounds + weight_ounces / 16

# Calculate unit price
unit_price = price_per_pound / 16

# Calculate total price
total_price = price_per_pound * weight_in_pounds

# Print the unit price and total price
print("Unit price: $" + str(unit_price))
print("Total price: $" + str(total_price))
