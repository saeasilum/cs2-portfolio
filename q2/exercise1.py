# Exercise 1: Count Even Numbers
# This script prints all even numbers between 2 and 20 using a for loop.
# (A for loop is used because the exact number of iterations is known.)

# The range() function follows three arguments:
# 1. Start value (2)
# 2. Stop value (21, so it includes 20)
# 3. Step value (2, adding 2 each time to select only even numbers)
for num in range(2, 21, 2):
    print(num)
