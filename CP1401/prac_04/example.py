MINIMUM_MONTH = 1
MAXIMUM_MONTH = 12

birth_month = int(input(f"Enter the month number ({MINIMUM_MONTH}-{MAXIMUM_MONTH}): "))
while birth_month < 1 or birth_month > 12:
    print("Invalid month")
    birth_month = int(input(f"Enter the month number ({MINIMUM_MONTH}-{MAXIMUM_MONTH}): "))

if birth_month <= 6:
    print("First half of the year")
else:
    print("Second half of the year")

for count in range(1, birth_month + 1):
    print(count, end=" ")
print()