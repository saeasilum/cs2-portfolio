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
