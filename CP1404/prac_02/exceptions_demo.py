"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
--- When the value entered is not an int or float

2. When will a ZeroDivisionError occur?
--- When the value of the denominator is 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))

    denominator = int(input("Enter the denominator: "))
    fraction = (numerator / denominator) if denominator else 0
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
