# Exercise 4: Multiplication Table Generator
# This script uses a function to print a multiplication table from 1 to 10 for a given number.

# Define the function that calculates and prints the table
def show_table(number):
    for i in range(1, 11):
        result = number * i # Multiply the input number by the current loop multiplier (i).
        print(f"{number} x {i} = {result}") # Print the equation and its calculated result using an f-string for formatting.

# Asks for a number and converts the user input into an integer
user_input = int(input("Enter a number: "))

# Passes the input number into the function as an argument
show_table(user_input)
