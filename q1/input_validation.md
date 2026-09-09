# Input Validation and Output Verification
**Activity:** PSHS Workshop Registration Validator  
**Name:** Sven Andrei E. Asilum
**Section:** Dahlia  
**Quarter:** 1  
---
## Activity Overview
In this activity, I created a program that validates information entered into a PSHS workshop registration
system.
The program checks whether user input satisfies specific requirements before accepting the registration.
The program validates:
- student name
- age
- grade level
- email address and
- registration code.

---
# Part A - Validation Requirements
| Data Captured | Expected Input | Validation Type | Invalid Input Example | Validation Rule | Error Message |
|---|---|---|---|---|---|
| Student Name | Text / String | Presence Check | `""` (empty entry) | Must not be blank | Reason: Student name is required. |
| Age | Integer | Data Type Check & Range Check | `"twelve"` or `10` | Must be a whole number between 11 and 18 inclusive | Reason: Age must be a number. / Reason: Age must be from 11 to 18. |
| Grade Level | Integer | Data Type Check & Range Check | `"grade 8"` or `6` | Must be a whole number between 7 and 12 inclusive | Reason: Grade level must be a number. / Reason: Grade level must be from 7 to 12. |
| Email Address | Text / String | Format / Domain Check | `student@gmail.com` | Must end with `@pshs.brc.edu.ph` | Reason: Invalid email domain. Must be a valid @pshs.brc.edu.ph address. |
| Registration Code | String | Length Check | `"12345"` or `"ABC1234"` | Must be exactly 6 characters long | Reason: The registration code must be exactly 6 characters. |
---
## Validation Questions
### 1. Why should the student name not be blank?
> The student name should not be blank to identify who is registering. Leaving it empty would create an invalid record, which would cause prevent proper student identification, cause database errors, and make the workshop attendance more difficult.
### 2. Why should age be checked for both data type and range?
> The age should be checked for both data type and range as checking the data type prevents the program from crashing if someone types letters, as for checking the data range makes sure the student is actually within the eligible age group (11 to 18) for the workshop.
### 3. Why should grade level only accept specific values?
> The grade level should only accept specific values 7 to 12 to ensure that only secondary school students currently enrolled within the target program are admitted.
### 4. What format requirements did you use for the email address?
> I converted the input to lowercase, stripped of whitespace, and that it must end with @pshs.brc.edu.ph to confirm the student belongs to the official school institution.
### 5. What length requirement did you use for the registration code?
> I used an exact string length of 6 characters (len(code) == 6) to match the standardized format.
---
# Part B - Program Design
## Pseudocode

```text
Function Main
    Declare String studentName
    Declare String ageInput
    Declare String gradeInput
    Declare String email
    Declare String registrationCode
    Declare Integer age
    Declare Integer gradeLevel

    Input studentName
    Input ageInput
    Input gradeInput
    Input email
    Input registrationCode
    If studentName == ""
        Output "========================================"
        Output "REGISTRATION NOT ACCEPTED"
        Output "========================================"
        Output "Reason: Student name is required."
    Else
        If isInteger(ageInput)
            Assign age = toInteger(ageInput)
            If age >= 11 and age <= 18
                If isInteger(gradeInput)
                    Assign gradeLevel = toInteger(gradeInput)
                    If gradeLevel >= 7 and gradeLevel <= 12
                        If endsWith(email, "@pshs.brc.edu.ph")
                            If len(registrationCode) == 6
                                Output "========================================"
                                Output "REGISTRATION ACCEPTED"
                                Output "========================================"
                                Output "Student Name : " & studentName
                                Output "Age          : " & age & " years old"
                                Output "Grade Level  : Grade " & gradeLevel
                                Output "Email        : " & email
                                Output "Reg. Code    : " & registrationCode
                            Else
                                Output "========================================"
                                Output "REGISTRATION NOT ACCEPTED"
                                Output "========================================"
                                Output "Reason: The registration code must be exactly 6 characters."
                            End
                        Else
                            Output "========================================"
                            Output "REGISTRATION NOT ACCEPTED"
                            Output "========================================"
                            Output "Reason: Invalid email domain. Must be a valid @pshs.brc.edu.ph address."
                        End
                    Else
                        Output "========================================"
                        Output "REGISTRATION NOT ACCEPTED"
                        Output "========================================"
                        Output "Reason: Grade level must be from 7 to 12."
                    End
                Else
                    Output "========================================"
                    Output "REGISTRATION NOT ACCEPTED"
                    Output "========================================"
                    Output "Reason: Grade level must be a number."
                End
            Else
                Output "========================================"
                Output "REGISTRATION NOT ACCEPTED"
                Output "========================================"
                Output "Reason: Age must be from 11 to 18."
            End
        Else
            Output "========================================"
            Output "REGISTRATION NOT ACCEPTED"
            Output "========================================"
            Output "Reason: Age must be a number."
        End
    End
End
```
---
# Part C - Program Implementation
## Programming Language
> Python
## Source Code File
[`workshop_validator.py`](workshop_validator.py)
## Final Code
``` PSHS Workshop Registration Validator

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
```

---
## Validation Techniques Used
### Presence Validation
> Presence Validation was used on the Student Name input `(studentName != "")` to ensure the field wasn't submitted blank. Checking that a non-empty name exists ensures that every registration record belongs to an identifiable student and prevents blank entries from entering the system.
### Data Type Validation
> Data Type Validation was applied to Age `(age_input)` and Grade Level `(grade_input)` using try-except blocks with int(). Trying to convert string inputs to integers within a try block safely handles non-numeric inputs without causing the program to throw an unhandled ValueError or crash.
### Range Validation
> I used range validation in Age and Grade Level using Python's chained comparison operators to keep entries strictly within bounds:
* Age: Checked using if not `(11 <= age <= 18):` to enforce ages from 11 to 18.    
* Grade Level: Checked using if not `(7 <= grade_level <= 12):` to enforce grades from 7 to 12.
### Acceptable Value Validation
> Acceptable value validation was applied during the Grade Level evaluation `(7 <= grade_level <= 12)` in order to restrict input strictly to secondary school levels (Grades 7, 8, 9, 10, 11, or 12). This rejects invalid numbers like 0, 67, or negative values that don't correspond to target student grade levels.
### Pattern Validation
> Pattern validation was implemented on the Email Address using `email.lower().endswith("@pshs.brc.edu.ph")`. Converting the email to lowercase and also checking its suffix ensures the user enters a valid school address and blocks outside domains.
### Length Validation
> Length validation was applied to the Registration Code using `len(registration_code) == 6.` Using Python's len() function ensures the string contains an exact count of 6 characters, matching the required code format.
---
# Part D - Testing
| Test | Input / Condition | Validation Being Tested | Expected Output | Actual Output | Result |
|---:|---|---|---|---|---|
| 1 | All inputs valid | Normal case | REGISTRATION ACCEPTED | REGISTRATION ACCEPTED | **PASS** |
| 2 | Blank student name | Presence | REGISTRATION NOT ACCEPTED - Reason: Student name is required. | REGISTRATION NOT ACCEPTED - Reason: Student name is required. | **PASS** |
| 3 | Age = `fourteen` | Data type | REGISTRATION NOT ACCEPTED - Reason: Age must be a number. | REGISTRATION NOT ACCEPTED - Reason: Age must be a number. | **PASS** |
| 4 | Age = `11` | Minimum boundary | REGISTRATION ACCEPTED | REGISTRATION ACCEPTED | **PASS** |
| 5 | Age = `18` | Maximum boundary | REGISTRATION ACCEPTED | REGISTRATION ACCEPTED | **PASS** |
| 6 | Age = `10` | Range | REGISTRATION NOT ACCEPTED - Reason: Age must be from 11 to 18. | REGISTRATION NOT ACCEPTED - Reason: Age must be from 11 to 18. | **PASS** |
| 7 | Grade Level = `13` | Acceptable value | REGISTRATION NOT ACCEPTED - Reason: Grade level must be from 7 to 12. | REGISTRATION NOT ACCEPTED - Reason: Grade level must be from 7 to 12. | **PASS** |
| 8 | Email = `studentpshs.edu.ph` | Pattern | REGISTRATION NOT ACCEPTED - Reason: Invalid email domain. Must be a valid @pshs.brc.edu.ph address. | REGISTRATION NOT ACCEPTED - Reason: Invalid email domain. Must be a valid @pshs.brc.edu.ph address. | **PASS** |
| 9 | Registration Code = `ABC` | Length | REGISTRATION NOT ACCEPTED - Reason: The registration code must be exactly 6 characters. | REGISTRATION NOT ACCEPTED - Reason: The registration code must be exactly 6 characters. | **PASS** |
| 10 | Registration Code = `CS2026` | Valid length | REGISTRATION ACCEPTED | REGISTRATION ACCEPTED | **PASS** |
---
# Part E - Output Verification
## Verification Test 1
**Input:**
```studentName = "Sven Asilum"
ageInput = "13"
gradeInput = "8"
email = "saeasilum@pshs.brc.edu.ph"
registrationCode = "451LUM"

```
**Expected Output:**
```========================================
REGISTRATION ACCEPTED
========================================
Student Name : Sven Asilum
Age          : 13 years old
Grade Level  : Grade 8
Email        : saeasilum@pshs.brc.edu.ph
Reg. Code    : 451LUM
```
**Actual Output:**
```========================================
REGISTRATION ACCEPTED
========================================
Student Name : Sven Asilum
Age          : 13 years old
Grade Level  : Grade 8
Email        : saeasilum@pshs.brc.edu.ph
Reg. Code    : 451LUM
```
**Result:** PASS    
**Explanation:**
> All inputs meet the required conditions (non-empty name, valid integer age within 11–18, valid integer grade within 7–12, correct institutional domain suffix, and an exact 6-character registration code). The program successfully displays the full student registration summary.
---
## Verification Test 2
**Input:**
```studentName = ""
ageInput = "14"
gradeInput = "9"
email = "saamolina@pshs.brc.edu.ph"
registrationCode = "M0L1N4"
```
**Expected Output:**
```========================================
REGISTRATION NOT ACCEPTED
========================================
Reason: Student name is required.
```
**Actual Output:**
```========================================
REGISTRATION NOT ACCEPTED
========================================
Reason: Student name is required.
```
**Result:** PASS    
**Explanation:**
> This is correct, as presence validation detects the blank name right away, stops the program, and displays the rejection message.
---
## Verification Test 3
**Input:**
```studentName = "Emmett Forest"
ageInput = "18"
gradeInput = "12"
email = "chiponmyshoulder@gmail.com"
registrationCode = "EMEF0R"
```
**Expected Output:**
```========================================
REGISTRATION NOT ACCEPTED
========================================
Reason: Invalid email domain. Must be a valid @pshs.brc.edu.ph address.
```
**Actual Output:**

```========================================
REGISTRATION NOT ACCEPTED
========================================
Reason: Invalid email domain. Must be a valid @pshs.brc.edu.ph address.
```
**Result:** PASS    
**Explanation:**
> This is correct, as pattern validation checks the email suffix and rejects the entry because @gmail.com does not match the required domain (@pshs.brc.edu.ph).
---
# Reflection
### 1. Why should a program validate input before processing it?
> A program should validate input before processing to prevent runtime errors, block invalid data from corrupting the system, and ensure the program only executes clean, predictable information.
### 2. What is the difference between input validation and output verification?
> The difference is that input validation checks if user data meets expected constraints before processing, while output verification checks if the program's final results match the expected output.
### 3. Which validation technique was easiest for you to implement? Why?
> For me, presence validation was the easiest because it only requires checking if an input string is blank or empty using basic equality or string length checks.
### 4. Which validation technique was most challenging? Why?
> Pattern validation was the most challenging for me because it requires precise string handling, such as lowercasing and checking specific domain suffixes, to ensure valid formatting.
### 5. How did testing invalid inputs help you improve your program?
> Testing invalid helped me improve my program by exposisng edge cases and potential bugs, helping refine the conditional logic to handle unexpected user inputs safely without crashing.

> `Drafted by me, with a quick assist from AI for grammar checking.`
---
# Files for This Activity
- [`workshop_validator.py`](workshop_validator.py)
- `input_validation.md`
---
[← Back to Main Portfolio](../README.md)
