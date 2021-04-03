"""
CP1401 2021-1 Assignment 1
Program 3 - Sleep Debt Calculator
Student Name: Braydan Newman
Date started: 21/3/2021
Date completed: 21/3/2021
Pseudocode:

    set desirable amount sleep
    set days of sleep

    for all days in days of sleep
        get sleep time
        while sleep time is valid
            display invalid number of hours
            get sleep time
        total sleep hours = total sleep hours + sleep time

    recommended total sleep = desirable amount sleep * days of sleep
    sleep debt = recommended total sleep - total sleep hours

    display recommended total sleep
    display total sleep hours

    if sleep debt > 0
        display sleep debt
    else
        display congratulations

"""

# Declare all consents
DESIRABLE_AMOUNT_SLEEP = 8
DAYS_OF_SLEEP = 5

total_sleep_hours = 0

# Adds up all days of sleep with error checking
for i in range(DAYS_OF_SLEEP):
    sleep_time = float(input(f"Night {i + 1} hours sleep: "))
    while sleep_time < 0  or sleep_time > 24:
        print("Invalid number of hours.")
        sleep_time = float(input(f"Night {i + 1} hours sleep: "))
    total_sleep_hours += sleep_time

# Calculate all necessary components
recommended_total_sleep = DESIRABLE_AMOUNT_SLEEP * DAYS_OF_SLEEP
sleep_debt = recommended_total_sleep - total_sleep_hours

# Display needed information
print(f"Recommended total sleep is: {recommended_total_sleep}")
print(f"Your total hours of sleep : {total_sleep_hours}")

# Decides whether to display congratulations or sleep dept
if sleep_debt > 0:
    print(f"Your sleep debt over this time is: {sleep_debt}")
else:
    print("You are getting enough sleep. Keep it up!")
