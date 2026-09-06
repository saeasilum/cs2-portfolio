# Clean Decision Code Makeover: Student Score Checker

## Part 1 - Analyze the Logic
**Input**  
A number entered by the user, stored as a `float` to work with decimals.

**Boundary Conditions**  
Minimum Valid Score: `0`  
Maximum Valid Score: `100`

**Possible Outputs**
1. `"Invalid score"`
2. `"Outstanding"`
3. `"Very Satisfactory"`
4. `"Satisfactory"`
5. `"Needs Improvement"`

**Selection Pattern - Boundary Condition**  
The initial check `if score < 0 or score > 100:` filters out invalid scores outside the 0–100 range.

**Selection Pattern - Multiple Decision Paths**  
The `elif` / `else` chain checks valid scores step-by-step from highest to lowest to assign the right grade category.
