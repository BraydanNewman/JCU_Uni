"""
CP1401 2021-1 Assignment 1
Program 1 – Pizza Pay Calculator
Student Name: Braydan Newman
Date started: 21/3/2021
Date completed: 21/3/2021
Pseudocode:

    set trip pay rate
    set minutes pay rate

    get number of trips
    get number of minutes

    total money from trips = number of trips * trip pay rate
    total money from minutes = number of minutes * minutes pay rate
    total money from all sources = total money from trips + total money from minutes

    display total money from trips
    display total money from minutes
    display total money from all sources

"""

# Declare all consents
TRIP_PAY_RATE = 1.45
MINUTE_PAY_RATE = 0.95

print("Warm Pizza Pay Calculator")

# Collect all user input
trips_taken = int(input("  Number of trips: "))
minutes_taken = int(input("Number of minutes: "))

# Calculates all necessary components
total_money_trips = trips_taken * TRIP_PAY_RATE
total_money_minutes = minutes_taken * MINUTE_PAY_RATE
total_money_pay = total_money_trips + total_money_minutes

# Display all needed information
print(f"For {trips_taken} trips, your pay is: ${total_money_trips:.2f}")
print(f"For {minutes_taken} minutes, your pay is: ${total_money_minutes:.2f}")
print(f"Your total pay is ${total_money_pay:.2f}")
