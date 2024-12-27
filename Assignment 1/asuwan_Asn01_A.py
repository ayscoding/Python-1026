""" 
CS1026a 2023
Assignment 01 Project 01 - Part A
9/29/2023
 
"""
# -----------------------------------------------------------
# Fibonacci Sequence (Finding the next value of 2 precedent values)
print("Project One <01> – Part A: Fibonacci Sequence \n")

# Prompt user to enter value
seq = int(input("Sequence ends at: "))

# Hard Coded Values
A = 0                                       
B = 1         

print("0:" , A , A)
print("1:" , B , B)

# Using for to find numbres in the range sequence
for i in range(2,seq+1):
    c = A + B
    print(f"{i}: {c} {c:,}")

    # Updating values for next loop
    A = B
    B = c

print()
print("END: Project One <01> – Part A")


   
    
    
    
 










