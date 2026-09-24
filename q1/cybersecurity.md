# Fundamentals of Cybersecurity and Data Privacy
**Activity:** PSHS Secure Club Registration System  
**Name:** Sven Andrei E. Asilum  
**Section:** Dahlia  
**Quarter:** 1  
---
## Activity Overview
In this activity, I analyzed a cybersecurity threat and developed secure data-capture rules for a simple
PSHS Club Registration System.
The goal is to create a program that collects only necessary information and accepts only correct,
expected, and appropriate input.
---
# Part A - Cybersecurity Threat Analysis
## Assigned Case **1:**
**Fake Login Alert:**
> A message claims that the student's account will be disabled and asks them to click a link and enter their
username and password.
---
### 1. What cybersecurity threat is shown?
> The cybersecurity threat shown is Phishing Attack / Social Engineering, which is an attempt to trick the user into revealing private login credentials through false urgency and manipulation.
### 2. What warning signs make the situation suspicious?
> Warning signs that make the situation suspicious are requesting credentials through an external and unverified link, rather through an official school authentication portal, and a high-pressure tactic creating artificial panic (threatening account suspension).
### 3. What may be affected?
- **Data:** Private user data, login credentials, and school records.
- **Account:** Student portal/school account access.
- **Device:** Can be potentially infected if the link leads to a malicious software.
- **Network:** The school network if compromised credentials are used to gain unauthorized internal access.
### 4. What information could be exposed or misused?
> Student account credentials, private school records, personal email communications, and class submissions.
### 5. What should the user do to reduce the risk?
> The user should verify account notifications directly by opening a trusted browser window and navigating to the official portal, report the message to school IT personnel, and never click links in unverified or unexpected security alerts.
---
# Part B - Data Privacy and Secure Data Capture
A proposed Club Registration System wants to collect the following information.
Determine whether each item is really necessary.
| Data | Collect / Do Not Collect | Reason |
|:---|:---|:---|
| Student Name | COLLECT | Required to identify and register the student. |
| Section | COLLECT | Required to verify class standing and schedule compatibility. |
| Club Choice | COLLECT | Required to place student into their chosen club group. |
| School Email | COLLECT | Required for official club announcements and communications. |
| Attendance Status | COLLECT | Required for tracking attendance during club periods. |
| Password | DO NOT COLLECT | Highly private and unnecessary. Registration forms do not require account access credentials. |
| OTP | DO NOT COLLECT | One-Time Passwords are strictly for multi-factor authentication and must never be gathered through a form. |
| Home Address | DO NOT COLLECT | Irrelevant to school club participation and poses an unnecessary privacy risk. | 
| Parent Bank Account | DO NOT COLLECT | Extremely high security risk and completely no relevance to joining a school club. |
---
## Privacy Question
Why is it safer to collect only information that the program actually needs?
> It is safer to collect only information that the program actually needs as it keeps user data safer because every piece of data stored is a risk. If a system gets hacked, leaked, or accessed by unauthorized people, any unnecessary information such as passwords, home addresses, or financial details, can be stolen and be misused to harm the user. By keeping data collection to a minimum, the system limits the amount of personal information exposed in the event of a security breach.
---
# Part C - Security-Focused Validation Rules
Complete the table before writing your program.
| Data Captured | Expected Input | Possible Risk | Invalid Input Example | Validation Rule | Error Message |
|:---|:---|:---|:---|:---|:---|
| Student Name | String (non-empty) | Anonymous/invalid record entry | `""` | Reject empty strings after whitespace trimming | `Error: Student name is required.` |
| Section | Valid section name (e.g. Dahlia) | Processing registrations from invalid/unlisted sections. | `Grade 8` | Must match one of the assigned/valid section names | `Error: Invalid section.` |
| Club Choice | Predefined club option (Robotics, Science, Mathematics, Programming) | Entering unsupported or unauthorized clubs | `Gaming` | Must be an item from the official club list | `Error: Please choose a valid club.` |
| School Email | Standard email format | Malformed address preventing notifications | `studentpshs.edu.ph`| Must contain @ and . characters | `Error: Invalid email format. Must contain '.' and '@'.` |
| Attendance Status | Valid status option (Present, Absent, Late) | Invalid or unrecognized attendance status | `Excused` | Must match one of the predefined attendance options | `Error: Invalid attendance status` |
---
## Secure Data Capture Questions
### 1. What should your program accept?
> The program should accept non-blank names, valid section names, valid choices from the designated club list, email addresses with proper `@` and `.`, structure, and exact attendance statues (`Present`, `Absent`, `Late`).
### 2. What should your program reject?
> The program should reject blank lines, unauthorized section names, non-listed clubs, malformed emails, unrecognized attendance entries, and any irrelevant private data.
### 3. How do your validation rules help reduce incorrect or unsafe input?
> The validation rules help reduce incorrect or safe input by acting as a filter. They catch blank inputs, typos, and bad data when the user enters them, stopping wrong information before it can break the program or mess up the system.
---
# Part D - Secure Program Implementation
## Program
Create a simple **PSHS Club Registration System**.
The program should collect only:
- Student Name
- Section
- Club Choice
- School Email Attendance Status
It should **not request passwords, OTPs, banking information, or unnecessary personal information**.
---
## Source Code File
[`secure_registration.py`](secure_registration.py)
---
## Final Code
```python
# PSHS Secure Club Registration System

def main():
    print("=== PSHS Secure Club Registration System ===\n")
    
    # 1. Student Name Validation (Must not be blank)
    student_name = input("Enter Student Name: ").strip()
    if not student_name:
        print("Error: Student name is required.")
        return
        
    # 2. Section Validation (Must match allowed section list)
    allowed_sections = [
        "Diamond", "Emerald", "Jade", "Sapphire", 
        "Dahlia", "Ilang-Ilang", "Rosal", "Sampaguita", 
        "Beryllium", "Magnesium", "Platinum", "Silicon", 
        "Electron", "Gluon", "Graviton", "Photon", 
        "Biology", "Chemistry", "Physics", "Bio-Chemistry"
    ]
    section = input("Enter Section: ").strip()
    matched_section = next((s for s in allowed_sections if s.lower() == section.lower()), None)
    if not matched_section:
        print("Error: Invalid section.")
        return
        
    # 3. Club Choice Validation (Must be from allowed list)
    allowed_clubs = ["Robotics", "Science", "Mathematics", "Programming"]
    club_choice = input("Enter Club Choice (Robotics, Science, Mathematics, Programming): ").strip()
    matched_club = next((c for c in allowed_clubs if c.lower() == club_choice.lower()), None)
    if not matched_club:
        print("Error: Please choose a valid club.")
        return
        
    # 4. School Email Validation (Must contain @ and .)
    school_email = input("Enter School Email: ").strip()
    if "@" not in school_email or "." not in school_email:
        print("Error: Invalid email format. Must contain @ and .")
        return
        
    # 5. Attendance Status Validation (Must be Present, Absent, or Late)
    allowed_attendance = ["Present", "Absent", "Late"]
    attendance_status = input("Enter Attendance Status (Present, Absent, Late): ").strip()
    matched_attendance = next((a for a in allowed_attendance if a.lower() == attendance_status.lower()), None)
    if not matched_attendance:
        print("Error: Invalid attendance status.")
        return
        
    # Success Output
    print("\n-----------------------------------")
    print("REGISTRATION ACCEPTED")
    print("-----------------------------------")
    print(f"Student: {student_name}")
    print(f"Section: {matched_section}")
    print(f"Club: {matched_club}")
    print(f"Email: {school_email}")
    print(f"Attendance: {matched_attendance}")
    print("-----------------------------------")

if __name__ == "__main__":
    main()
```
---
## Security Practices Applied
### Required Input
> I handled the blank inputs by applying `.strip()` to remove leading/trailing spaces and using conditional checks (`if not input_val`) to stop the program and display an error message if any field is left empty.
### Allowed Values
> Restricted fields like Section, Club Choice, and Attendance status follow specific lists of predefined values. Inputs are checked against these lists using case-insensitive matching before being accepted.
### Format Check
> I checked school email inputs by verifying that both `@` and `.` exist in the entered string before approving registration.
### Error Messages
> Error messages are useful because when an input fails validation, it gives the user direct feedback without crashing or exposing system internals.
### Data Minimization
> I did not collect information such as passwords, OTPs, home addresses, or financial details because they are completely unnecessary for joining a school club. Not collecting them protects student privacy and ensures that even if registration data is leaked or accessed without permission, no private data would be exposed.
---
# Part E - Testing and Reflection
## Testing
| Test | Input Situation | Expected Output | Actual Output | Result |
|---:|---|---|---|---|
| 1 | All data valid | REGISTRATION ACCEPTED | REGISTRATION ACCEPTED | **PASS** |
| 2 | Blank student name | Rejected | Error: Student name is required. | **PASS** |
| 3 | Invalid section | Rejected | Error: Invalid section. | **PASS** | 
| 4 | Invalid club choice | Rejected | Error: Please choose a valid club. | **PASS** |
| 5 | Email missing `@` | Rejected | Error: Invalid email format. Must contain `@` and `.` | **PASS** |
| 6 | Email missing `.` | Rejected | Error: Invalid email format. Must contain `@` and `.` | **PASS** |
| 7 | Invalid attendance status | Rejected | Error: Invalid attendance status. | **PASS** |
| 8 | Different valid inputs | REGISTRATION ACCEPTED | REGISTRATION ACCEPTED | **PASS** |
Use:
- **PASS** if the actual result matches the expected result.
- **FAIL** if it does not.
---
# Reflection
### 1. What is one cybersecurity threat that can affect an application or user?
> One cybersecurity threat that can affect an application or user is phishing, where attackers trick users into entering private information such as login credentials or personal information on fake links or deceptive sites.
### 2. How can users reduce the risk of phishing or suspicious messages?
> Users can reduce the risk of phishing or suspicious messages by avoiding clicking unverified external links, checking sender details carefully, not sharing passwords/OTPs, and double-checking suspicious alerts before taking action.
### 3. How can validation rules improve the security of user input?
> Validation rules improve the security of user input by acting as a filter at the program boundary. They make sure only safe and properly formatted data is accepted while blocking malformed or unexpected input before it can cause errors or vulnerabilities.
### 4. Why should a program avoid collecting unnecessary personal information?
> A program should avoid collecting unnecessary personal information because that data can be stolen if the program is ever hacked or leaked. By keeping data collection to only what is necessary, the program keeps student information safe and limits any potential harm.
### 5. How did SG7's input validation concepts become security practices in SG8?
> Input validation originally prevented program crashes caused by basic user mistakes, such as typing letters into a number field; but it then turned into a security defense that protects system integrity, blocks unsafe or unexpected data from entering the application, and enforces privacy by keeping user data strictly controlled.
---
# Files for This Activity
- [`secure_registration.py`](secure_registration.py)
- `cybersecurity.md`
---
[← Back to Main Portfolio](../README.md)
