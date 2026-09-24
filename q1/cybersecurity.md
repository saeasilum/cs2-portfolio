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
| Data Captured | Expected Input | Possible Risk | Invalid Input Example | Validation Rule | Error
Message |
|:---|:---|:---|:---|:---|:---|
| Student Name | String (non-empty) | Anonymous/invalid record entry | `""` | Reject empty strings after whitespace trimming | `Error: Student name is required.` |
| Section | Valid section name (e.g. Dahlia) | Processing registrations from invalid/unlisted sections. | `Grade 8` | Must match one of the assigned/valid section names | `Error: Invalid section name.` |
| Club Choice | Predefined club option | Entering unsupported or unauthorized clubs | `Gaming` | Must be an item from the official club list | `Error: Please choose a valid club. |
| School Email | | | | | |
| Attendance Status | | | | | |
---
## Secure Data Capture Questions
### 1. What should your program accept?
> Write your answer here.
### 2. What should your program reject?
> Write your answer here.
### 3. How do your validation rules help reduce incorrect or unsafe input?
> Write your answer here.
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
# Paste your final program here.
```
---
## Security Practices Applied
### Required Input
> Explain how you handled blank input.
### Allowed Values
> Explain which fields accept only predefined values.
### Format Check
> Explain your simple email validation rule.
### Error Messages
> Explain why clear error messages are useful.
### Data Minimization
> Explain what information you intentionally did NOT collect and why.
---
# Part E - Testing and Reflection
## Testing
| Test | Input Situation | Expected Output | Actual Output | Result |
|---:|---|---|---|---|
| 1 | All data valid | | | |
| 2 | Blank student name | | | |
| 3 | Invalid section | | | | | 4 | Invalid club choice | | | |
| 5 | Email missing `@` | | | |
| 6 | Email missing `.` | | | |
| 7 | Invalid attendance status | | | |
| 8 | Different valid inputs | | | |
Use:
- **PASS** if the actual result matches the expected result.
- **FAIL** if it does not.
---
# Reflection
### 1. What is one cybersecurity threat that can affect an application or user?
> Write your answer here.
### 2. How can users reduce the risk of phishing or suspicious messages?
> Write your answer here.
### 3. How can validation rules improve the security of user input?
> Write your answer here.
### 4. Why should a program avoid collecting unnecessary personal information?
> Write your answer here.
### 5. How did SG7's input validation concepts become security practices in SG8?
> Write your answer here.
---
# Files for This Activity
- [`secure_registration.py`](secure_registration.py)
- `cybersecurity.md`
---
[← Back to Main Portfolio](../README.md)
