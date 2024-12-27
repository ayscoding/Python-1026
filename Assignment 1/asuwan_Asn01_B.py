""" 
CS1026a 2023
Assignment 01 Project 01 - Part B
9/29/2023
 
"""
# -------------------------------------------------
# Finding prime numbres 

# Opening Message
print("Project One <01> – Part B: Prime Choice")
print()
import math

# Prompt User to Enter Values
start_P = int(input("Prime numbers starting with: "))
end_P = int(input("and ending with: "))

# Range Conditional Statemet
if start_P > end_P:
    print(f"\nIncorrect input: {start_P} is greater than {end_P} \nThe numbers have been automatically switched" )
    start_P, end_P = end_P, start_P
print (f"\nPrime numbers in the range from: {start_P} and {end_P} are: ")

# Using a loop for range of values between provided numbers
for i in range(start_P, end_P+1):

    if i <= 1:
        continue                     # if true skips after, and starts over

    root_d = int(math.sqrt(i))
    is_prime = True

    for k in range(2,root_d+1):           # Applying prime numbre validation
        if i % k == 0:
            is_prime = False
            continue

    if is_prime:                        # Prints the number if satisfied
        print(f"{i} is prime")  
print()
print("END: Project One <01> – Part B")
