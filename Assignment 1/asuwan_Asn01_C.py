""" 
CS1026a 2023
Assignment 01 Project 01 - Part C
9/29/2023
 
"""
# -------------------------------------------------------------
# The Moore the Merrier
# Opening Message
print("Project One <01> – Part C: The Moore the Merrier\n")

# Prompt user to enter variables
start_n = int(input("Starting number of transistors: "))
start_y = int(input("Starting year: "))
total_Y = int(input("Total number of years: "))

# Calculate the total years
sum_Tot = start_y + total_Y

# Hard-coded value
FACTOR = 50

print("\nYEAR  TRANSISTORS  FLOPS")

# Assigning value units
def flop_string(w):
    if len(str(w)) <= 3:
        return "FLOPS"
    elif len(str(w)) <= 6:
        return "kiloFLOPS"
    elif len(str(w)) <= 9:
        return "megaFLOPS"
    elif len(str(w)) <= 12:
        return "gigaFLOPS"
    elif len(str(w)) <= 15:
        return "teraFLOPS"
    elif len(str(w)) <= 18:
        return "petaFLOPS"
    elif len(str(w)) <= 21:
        return "exaFLOPS"
    elif len(str(w)) <= 24:
        return "zettaFLOPS"
    else:
        return "yottaFLOPS"

# Assigning decimals
def convert_num(num):
    c = str(num)
    if len(c) <= 3:
        return int(c)
    elif len(c) <= 6:
        return int(c) / 10 ** 3  # Kilo
    elif len(c) <= 9:
        return int(c) / 10 ** 6  # Mega
    elif len(c) <= 12:
        return int(c) / 10 ** 9  # Giga
    elif len(c) <= 15:
        return int(c) / 10 ** 12  # Tera
    elif len(c) <= 18:
        return int(c) / 10 ** 15  # Peta
    elif len(c) <= 21:
        return int(c) / 10 ** 18  # Exa
    elif len(c) <= 24:
        return int(c) / 10 ** 21  # Zetta
    else:
        return int(c) / 10 ** 24  # Yotta

# Starting a while loop
while start_y <= sum_Tot:
    q = start_n * FACTOR  # FLOPS
    name = flop_string(q)  # Calling the function to assign a unit and store it
    num = convert_num(q)  # Calling the function to adjust decimal position

    # Prints the values
    print(f"{start_y} {start_n:,} {num:.2f} {name} {q:,}")

    # Assigning new values
    start_y = start_y + 2
    start_n = start_n * 2

print("\nEND: Project One <01> – Part C")

