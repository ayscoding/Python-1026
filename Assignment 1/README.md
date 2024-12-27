## Fibonacci Sequence Program (asn01_A.py)

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

<br>

## Prime Number Finder (asn01_B.py)

This Python file is part of **Project 01** and identifies all prime numbers within a user-specified range. The program ensures proper handling of user input and efficiently validates primality using mathematical optimization.

### Features
- **User Input for Range**: 
  - The program prompts the user to enter a starting value (`from`) and an ending value (`to`) to define the range.
  - For example, to find all prime numbers between `3` and `11`, the user inputs `3` and `11`.

- **Input Validation and Error Handling**:
  - If the starting value is greater than the ending value, the program automatically switches the values to ensure a valid range and notifies the user of the correction.

- **Optimized Prime Number Validation**:
  - Numbers less than or equal to `1` are skipped since they are not prime.
  - For each number in the range, the program checks for divisors up to the square root of the number (an efficient approach for primality testing).
  - If a number is determined to be prime, it is displayed in the format `{number} is prime`.

- **Output Format**:
  - The program displays:
    1. The corrected range (if applicable).
    2. A list of prime numbers in the specified range, each line formatted as `{number} is prime`.
  - Includes a clear end message signaling the program's completion.

### Example Output
If the user inputs a range of `11` to `3`, the program will:
1. Automatically switch the range to `3` to `11`.
2. Output:
3 is prime
5 is prime
7 is prime
11 is prime

<br>

## Moore's Law Estimation Program

This Python file is part of **Project 01** and implements Moore's Law to estimate the growth in computing power over time. Moore's Law states that the number of transistors in an integrated circuit doubles approximately every two years, leading to exponential increases in computational performance.

### Features
- **User Input**:
  - The program prompts the user to input:
    1. The **starting number of transistors**.
    2. The **starting year** for calculations.
    3. The **total number of years** for which the calculations should be performed.

- **Computational Logic**:
  - The program calculates the growth of transistors over a series of 2-year increments, doubling the number of transistors every two years as per Moore's Law.
  - For each year, it calculates the **computing power (FLOPS)** by multiplying the current number of transistors by a constant factor of `50`.

- **Unit Conversion and Output Formatting**:
  - The computing power is displayed using appropriate units such as `FLOPS`, `kiloFLOPS`, `megaFLOPS`, etc., depending on its magnitude.
  - For readability, the output includes:
    1. The **current year**.
    2. The **number of transistors**, formatted with commas.
    3. The computing power displayed in:
       - Scaled units with 2 decimal places (e.g., `5.00 kiloFLOPS`).
       - Raw number format (e.g., `5,000 FLOPS`).

- **Output Format**:
  - Example output based on the inputs `Starting number of transistors: 100`, `Starting year: 2023`, and `Total number of years: 6`:
    ```
    YEAR  TRANSISTORS  FLOPS
    2023 100 5.00 kiloFLOPS 5,000
    2025 200 10.00 kiloFLOPS 10,000
    2027 400 20.00 kiloFLOPS 20,000
    2029 800 40.00 kiloFLOPS 40,000

    END: Project One <01> – Part C
    ```

### Educational Purpose
This program demonstrates:
- **Exponential growth modeling** using Moore's Law.
- **Efficient calculations** involving large numerical values.
- **Dynamic unit scaling** for better representation of results.
- **Readable and well-formatted output**, suitable for understanding large-scale computations.

### Notes
- The unit definitions follow FLOPS scaling:
  - `1,000 FLOPS = 1 kiloFLOPS`, `1,000 kiloFLOPS = 1 megaFLOPS`, and so on.
- The program handles calculations up to `YottaFLOPS`.
- Designed to provide both numerical precision and a clear understanding of exponential growth trends.
