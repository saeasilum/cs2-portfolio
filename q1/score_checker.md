# Clean Decision Code Makeover: Student Score Checker
**Name:** Sven Andrei E. Asilum    
**Section:** Dahlia    
---
## Activity Overview

In this activity, I improved a Student Score Checker program by applying proper coding standards and selection structures.
The program accepts a student score from 0 to 100 and determines the appropriate classification.

The classifications are:
| Score | Classification |
|---|---|
| 90-100 | Outstanding |
| 80-89 | Very Satisfactory |
| 75-79 | Satisfactory |
| 0-74 | Needs Improvement |

Scores below 0 or above 100 are considered invalid.
---
# Part 1 - Analyze the Logic
## Input 
What information does the program need? 
> A number entered by the user, stored as a `float` to work with decimals.

## Valid Range 
**Minimum valid score:**    
> `0`    
**Maximum valid score:**    
> `100`

## Possible Outputs
1. `"Invalid score"`
2. `"Outstanding"`
3. `"Very Satisfactory"`
4. `"Satisfactory"`
5. `"Needs Improvement"`

## Boundary Condition 
> The initial check `if score < 0 or score > 100:` filters out invalid scores outside the 0–100 range.

## Multiple Decision Paths 
> The `elif` / `else` chain checks valid scores step-by-step from highest to lowest to assign the right grade category.
---
## Flowchart
![Score Checker Flowchart](flowchart.png)
---
## Pseudocode
```text
Function Main
    Declare Real score

    Input score
    If score < 0 or score > 100
        Output "Invalid score"
    Else
        If score >= 90
            Output "Outstanding"
        Else
            If score >= 80
                Output "Very Satisfactory"
            Else
                If score >= 75
                    Output "Satisfactory"
                Else
                    Output "Needs Improvement"
                End
            End
        End
    End
End
```
---
# Part 4 - Clean Code Implementation 
## Source code 
[Score Checker Source Code](score_checker.py)

---
## Testing & Validation

| Test | Input | Purpose | Expected Output | Actual Output | Result |
| :---: | :---: | :--- | :--- | :--- | :---: |
| 1 | -1 | Below minimum | Invalid score | Invalid score | Pass |
| 2 | 0 | Minimum boundary | Needs Improvement | Needs Improvement | Pass |
| 3 | 74 | Below Satisfactory boundary | Needs Improvement | Needs Improvement | Pass |
| 4 | 75 | Satisfactory boundary | Satisfactory | Satisfactory | Pass |
| 5 | 80 | Very Satisfactory boundary | Very Satisfactory | Very Satisfactory | Pass |
| 6 | 90 | Outstanding boundary | Outstanding | Outstanding | Pass |
| 7 | 100 | Maximum boundary | Outstanding | Outstanding | Pass |
| 8 | 101 | Above maximum | Invalid score | Invalid score | Pass |
---
# Testing Reflection 
### 1. Why is it important to test the values 0 and 100? 
> It is important in order to make sure the program accepts the minimum and maximum passing/valid grades without giving an error.
### 2. Why did you also test -1 and 101? 
> I tested -1 and 101 to check if the program successfully rejects numbers that go below or above the allowed limit.
### 3. Which test helped you understand boundary conditions the most? 
> Testing 75, 80, and 90 helped me most as it showed how inclusive operators (`>=`) handle the exact cutoff scores.
### 4. Did any of your tests initially fail? If yes, what did you change in your program? 
> Yes, the invalid score tests initially failed because I wrote < 0 score < 100 by mistake instead of using the proper logical operators. This resulted in numbers greater than 100 being a valid number. I fixed it by changing the condition to score < 0 or score > 100 so that it correctly flags numbers outside the 0–100 range.
---
# Reflection
### 1. How did selection structures make the program more useful? 
> Selection structures allow the program to check different score ranges and print the right classification instead of running every line in order.
### 2. How did proper comments and readable formatting improve your program? 
> Proper comments and readable formatting make the code easy to read and help spot logic mistakes quickly.
### 3. Why is it useful to plan the program using a flowchart and pseudocode before writing the code? 
> It is useful to plan the program using a flowchart and pseudocode before writing the code as it gives a clear visual guide of how the conditions branch out, which saves time when translating it into Python.
