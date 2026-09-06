# PSHS Student Code Checker
# This program will assess a student's score and decide their performance level.

# Ask the user to input a score
score = float(input("Enter student score: "))

# Check if score is less than 0 or greater than 100
if score < 0 or score > 100:
  print("Invalid Score.")

# Classify the valid scores
elif score >= 90:
  print("Outstanding")
elif score >= 80:
  print("Very Satisfactory")
elif score >= 75:
  print("Satisfactory")
else: 
  print("Needs Improvement")
