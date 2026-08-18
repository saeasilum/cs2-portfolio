import math

# Step 1 - Ask the user to input the coordinates
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Step 2 - Calculate the distance using math.sqrt() and math.pow()
distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

# Step 3 - Display the answer rounded to two decimal places
print(f"The distance between the two points is: {distance:.2f}")

# Reflection
# The math library simplified my program by providing ready-to-use functions for the square root and power operations.
# Using math.sqrt() and math.pow() allowed me to write the Euclidean distance formula in a single and clear line of code.
# Without these built-in functions, we would have to write custom algorithms from scratch just to compute the square roots and powers.
