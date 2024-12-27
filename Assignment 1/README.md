## Fibonacci Sequence Program

This Python file is part of **Project 01** and calculates the Fibonacci sequence. The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding numbers, starting with `0` and `1`. This sequence is widely used in mathematics, science, and computer science for various applications.

### Features
- **Hardcoded Base Cases**: The first two terms of the sequence (`0` and `1`) are predefined and displayed directly.
- **Recursive Formula**: Subsequent terms are calculated using the formula:  
  `x_n = x_(n-1) + x_(n-2)` (for `n > 1`).
- **User Input**: The program calculates the sequence up to a number specified by the user.
- **Formatted Output**: Each term is displayed in the following format:
  - `{Sequence Number}: {Value}` (e.g., `20: 6765`)
  - The values are also formatted with commas for readability (e.g., `6,765`).

### Example Output
If the user chooses to calculate up to the 21st Fibonacci number, the output will include:
20: 6765 6,765