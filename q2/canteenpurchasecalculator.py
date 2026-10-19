# Problem 1: The Canteen Purchase Calculator

# Function 1: Calculates the total purchase cost
def calculate_total(price, quantity):
    return price * quantity

# Function 2: Calculates the change or shortage
def calculate_change(payment, total):
    return payment - total

# 1. Ask the user for the item's price, quantity, and the payment
price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))
payment = float(input("Enter amount paid: "))

# 2 & 3. Pass the price and quantity to calculate_total() and store the returned total in a variable
total_cost = calculate_total(price, quantity)
print(f"Total Cost: PHP {total_cost:.2f}")

# 4. Pass the payment and the computed total to calculate_change()
change_result = calculate_change(payment, total_cost)

# 6. Display the change, or if payment is insufficient, display the additional amount needed
if change_result >= 0:
    print(f"Change: PHP {change_result:.2f}")
else:
    # If the change is negative, make it positive to show the shortage amount
    shortage = abs(change_result)
    print(f"Insufficient payment! Additional amount needed: PHP {shortage:.2f}")

# ==========================================
# DOCUMENTATION QUESTIONS & ANSWERS
# ==========================================
# 1. What does each function do?
# - calculate_total(price, quantity): This function multiplies the item price by the quantity purchased to return the overall total cost. 
# - calculate_change(payment, total): This function subtracts the total cost from the amount paid by the customer to find out how much change to return. 
# 2. What is the difference between the parameters price and quantity and the actual arguments passed to the function?
# - The difference between the parameters price and quantity and the actual arguments passed to the function is that parameters (price and quantity) are the placeholder variables inside the function definition, while arguments are the actual values or variables passed into the function when called.
# 3. Where is the returned total stored, and how is it reused?
# - The returned total is stored in the variable 'total_cost', and it is reused later by being passed into the calculate_change() function and by being printed out.
# 4. Why is it useful to separate total calculation from change calculation?
# - It is useful to separate total calculation from change calculation as this keeps the code organized, easier to read, and simpler to debug. 
