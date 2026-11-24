# Exercise 2: Travel Destination Manager
# This script stores five travel destinations in a list and lets the user view, search, and update them.

# Create a list containing five travel destinations (indices 0 to 4)
destinations = ["Cebu", "Manila", "Davao", "Baguio", "Palawan"]

# Display all destinations using a for loop
print("===ALL TRAVEL DESTINATIONS===")
for place in destinations:
    print(place)

print()

# Use list slicing to get items from index 1 up to (but not including) index 4
sliced_destinations = destinations[1:4]
print("Destinations from index 1 to 3:", sliced_destinations)

print()

# Ask the user to enter a destination to search for
search_place = input("Enter a destination to search for: ")

# Check if the entered destination exists in the list
if search_place in destinations:
    print(f"{search_place} is in the destinations list.")
else:
    print(f"{search_place} is not in the destinations list.")

print()

# Replace the item at index 2 ("Davao") with "Iloilo"
destinations[2] = "Iloilo"

# Display the updated list
print("Updated destinations list:", destinations)
