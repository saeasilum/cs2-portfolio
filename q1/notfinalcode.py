# PSHS Workshop Registration Validator

# Input name
while True:
      student_name = input("Enter name: ").strip()
      if student_name != "":
          break
      else:
          print("Student name is required.")

# Input age
while True:
    try:
      age = int(input("Enter Age: "))
      if 11 <= age <= 18:
        break
      else:
        print("Age must be from 11 to 18. Please try again.")
  
    except ValueError:
      print("Age must be a number. Please try again.")

# Input grade level
while True:
  try:
    grade_level = int(input("Enter Grade Level: "))
    if 7 <= grade_level <= 12:
       break
    else:
      print("Grade level must be from 7 to 12. Please try again.")

  except ValueError:
      print("Grade level must be a number. Please try again.")

# Input Email
while True:
    email = input("Enter Email: ").strip().lower()
    if email.endswith("@pshs.brc.edu.ph"):
      break
    else:
        print("Invalid email. Must be a valid @pshs.brc.edu.ph address. Please try again.")

# Input Registration code
while True:
  registration_code = input("Enter Registration Code: ").strip()
  if len(registration_code) == 6:
      break
  else:
      print("The registration code must be exactly 6 digits. Please try again.")

# Display Final Registration Results
print("\n" "------------------------------")
print("REGISTRATION ACCEPTED")
print("------------------------------")
print(f"Student Name : {student_name}")
print(f"Age          : {age} years old")
print(f"Grade Level  : Grade {grade_level}")
print(f"Email        : {email}")
print(f"Reg. Code    : {registration_code}")
