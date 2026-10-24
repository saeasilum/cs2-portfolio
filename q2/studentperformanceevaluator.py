# Problem 2: Student Performance Evaluator

# Calculates the numerical average of three scores
def calculate_average(score1, score2, score3):
    return (score1 + score2 + score3) / 3

# Determines the performance category as a string based on the average score
def get_performance(average):
    if average >= 85 and average <= 100:
        return "Mastery"
    elif average >= 70 and average < 85:
        return "Developing"
    else:
        return "Needs Review"

# Returns True or False (Boolean) for challenge eligibility
def is_eligible(average, completed_tasks):
    if average >= 85 and completed_tasks >= 3:
        return True
    else:
        return False

# 1. Ask the user to enter three scores between 0 and 100
score1 = float(input("Enter Score 1: "))
score2 = float(input("Enter Score 2: "))
score3 = float(input("Enter Score 3: "))

# 2. Ask for the number of completed tasks, from 0 to 5
completed_tasks = int(input("Completed Tasks: "))

# 3. Use calculate_average() to compute the average
avg = calculate_average(score1, score2, score3)

# 4. Pass the returned average as an argument to get_performance()
performance = get_performance(avg)

# 5. Pass the average and number of completed tasks to is_eligible()
eligible = is_eligible(avg, completed_tasks)

# 6. Display the average, performance category, and eligibility result
print(f"Average: {avg:.2f}")
print(f"Performance: {performance}")
print(f"Eligible for Challenge: {eligible}")

# ==========================================
# DOCUMENTATION QUESTIONS & ANSWERS
# ==========================================
# 1. Which function returns a number, which returns a string, and which returns a Boolean?
# - calculate_average() returns a numerical average. 
# - get_performance() returns a string representing the performance category. 
# - is_eligible() returns a Boolean value (True or False). 

# 2. Explain how the average moves from calculate_average() into get_performance().
# - The calculate_average() function computes the value and then sends it back using the return statement. That returned value is stored in a variable, which is then passed as an argument into get_performance(). 

# 3. What happens when a student has a high average but has completed fewer than three tasks?
# - If a student has a high average but has completed fewer than three tasks, then the student will not be eligible for the practice challenge. (This is because the is_eligible() function requires both conditions to be met (an average of at least 85 AND at least 3 completed tasks)). 

# 4. Why is return more appropriate than simply printing the result inside each function?
# - Using return is more appropiate than simply printing the result inside each function as it sends the data back to the main program so it can be stored in variables and reused. Simply printing only displays the text on the screen and does not allow other functions or conditional statements to access that value.
