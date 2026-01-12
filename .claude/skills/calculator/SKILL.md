---
name: calculator
description: CRITICAL for ALL mathematical and numerical operations including arithmetic, percentages, averages, and DATE/CALENDAR calculations (day of week, date differences, time calculations). MANDATORY when user asks to calculate, compute, solve expressions, determine dates, or perform any numeric analysis.
---

# Calculator Skill

## Instructions
1. Parse the mathematical expression carefully
2. Follow standard order of operations (PEMDAS/BODMAS)
3. Show your work step-by-step for complex calculations
4. Provide the final result with appropriate precision
5. If the expression is ambiguous, clarify with the user before calculating

## Examples

### Example 1: Basic Calculation
**User:** "What's 15% of 250?"
**Action:** Calculate: 250 × 0.15 = 37.5
**Response:** "15% of 250 is 37.5"

### Example 2: Complex Expression
**User:** "Calculate (45 + 27) × 3 - 12 / 4"
**Action:** 
- First: (45 + 27) = 72
- Then: 12 / 4 = 3
- Then: 72 × 3 = 216
- Finally: 216 - 3 = 213
**Response:** "The result is 213"

### Example 3: Multiple Operations
**User:** "If I buy 3 items at $24.99 each and 2 items at $12.50 each, what's the total?"
**Action:** 
- 3 × $24.99 = $74.97
- 2 × $12.50 = $25.00
- Total: $74.97 + $25.00 = $99.97
**Response:** "The total cost is $99.97"

## Error Handling
- Division by zero: Inform user this is undefined
- Invalid expressions: Ask for clarification
- Very large numbers: Use scientific notation when appropriate