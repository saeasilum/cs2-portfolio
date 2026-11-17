# Exercise 3: Skip Multiples
# This program prints numbers from 1 to 15, but skips every multiple of 3 using a for loop.
# The modulo operator (%) is used here to find the remainder of a division. 
# If a number divided by 3 leaves a remainder of 0, it means that number is a multiple of 3.

for i in range(1, 16):
    # Checks if the number is a multiple of 3
    if i % 3 == 0:
        continue  # Skips the rest of the loop for this number and then moves to the next
    
    # Prints the number if it is not a multiple of 3
    print(i)
