# PSHS Workshop Registration Validator

# Collect all inputs
student_name = input("Enter name: ").strip()
age_input = input("Enter Age: ").strip()
grade_input = input("Enter Grade Level: ").strip()
email = input("Enter Email: ").strip().lower()
registration_code = input("Enter Registration Code: ").strip()

# 1. Validate Name
if not student_name:
    print("\n" + "=" * 40)
    print("REGISTRATION NOT ACCEPTED")
    print("=" * 40)
    print("Reason: Student name is required.")
    exit()

# 2. Validate Age
try:
    age = int(age_input)
    if not (11 <= age <= 18):
        print("\n" + "=" * 40)
        print("REGISTRATION NOT ACCEPTED")
        print("=" * 40)
        print("Reason: Age must be from 11 to 18.")
        exit()
except ValueError:
    print("\n" + "=" * 40)
    print("REGISTRATION NOT ACCEPTED")
    print("=" * 40)
    print("Reason: Age must be a number.")
    exit()

#3. Validate Grade Level
try:
  grade_level = int(grade_input)
  if not (7 <= grade_level <= 12):
    print("\n" + "=" * 40)
    print("REGISTRATION NOT ACCEPTED")
    print("=" * 40)
    print("Reason: Grade level must be from 7 to 12.")
    exit()
except ValueError:
    print("\n" + "=" * 40)
    print("REGISTRATION NOT ACCEPTED")
    print("=" * 40)
    print("Reason: Grade level must be a number.")
    exit()

# 4. Validate Email
if not email.endswith("@pshs.brc.edu.ph"):
    print("\n" + "=" * 40)
    print("REGISTRATION NOT ACCEPTED")
    print("=" * 40)
    print("Reason: Invalid email domain. Must be a valid @pshs.brc.edu.ph address.")
    exit()

# 5. Validate Registration Code
if len(registration_code) != 6:
    print("\n" + "=" * 40)
    print("REGISTRATION NOT ACCEPTED")
    print("=" * 40)
    print("Reason: The registration code must be exactly 6 characters.")
    exit()

# Display Final Registration Results if all checks pass
print("\n" + "=" * 40)
print("REGISTRATION ACCEPTED")
print("=" * 40)
print(f"Student Name : {student_name}")
print(f"Age          : {age_input} years old")
print(f"Grade Level  : Grade {grade_level}")
print(f"Email        : {email}")
print(f"Reg. Code    : {registration_code}")
