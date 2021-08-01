"""
CP1401 2021-1 Assignment 2
Market Garden Simulator
Student Name: Braydan Newman
Date started: 10/5/2021
Pseudocode:
    LOW_RAINFALL_THRESHOLD = 30

    Display start_message

    Initialise List plants
    Initialise Integer food
    Initialise Integer day_count

    While True
        Display users stats
        Display menu

        Get choice from user

        If choice Is wait day
            Increment day_count
            Check rain_amount

            If rain_amount is below low_rainfall_threshold
                Delete plant is plants list

            Calculate food_produced From plants
            Add food_produced to food

        Else If choice Is display Plants
            Display plants

        Else If choice Is add plant
            Get plant_name from user

            If plant_name Is Valid
                Add plant_name to plants
            Else
                Display invalid plant name

        Else If choice Is quit
            Break Out Of Loop

        Else
            Display invalid choice

    Display quit dialog
"""

import random

# Set constants
RAIN_ART = """                             000      00
                           0000000   0000
              0      00  00000000000000000
            0000 0  000000000000000000000000       0
         000000000000000000000000000000000000000 000
        0000000000000000000000000000000000000000000000
    000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000
              / / / / / / / / / / / / / / / /
            / / / / / / / / / / / / / / /
            / / / / / / / / / / / / / / /
          / / / / / / / / / / / / / /
          / / / / / / / / / / / / /
        / / / / / / / / / / / /
        / / / / / / / / / /"""

TITLE_TEXT = """  __  __             _         _      ___                _              ___  _              _        _             
 |  \/  | __ _  _ _ | |__ ___ | |_   / __| __ _  _ _  __| | ___  _ _   / __|(_) _ __  _  _ | | __ _ | |_  ___  _ _ 
 | |\/| |/ _` || '_|| / // -_)|  _| | (_ |/ _` || '_|/ _` |/ -_)| ' \  \__ \| || '  \| || || |/ _` ||  _|/ _ \| '_|
 |_|  |_|\__,_||_|  |_\_\\___| \__|  \___|\__,_||_|  \__,_|\___||_||_| |___/|_||_|_|_|\_,_||_|\__,_| \__|\___/|_|  """

WELCOME = """
Welcome to the Market Garden Simulator
Plants cost and generate food according to their name length (e.g., Sage plants cost 4).
You can buy new plants with the food your garden generates.
You get up to 100 mm of rain per day. Not all plants can survive with less than 30.
Let's hope it rains... a lot!
You start with these plants:
"""

MENU = """
(W)ait
(D)isplay plants
(A)dd new plant
(Q)uit
"""

MIN_RAINFALL = 0
MAX_RAINFALL = 100
LOW_RAINFALL_THRESHOLD = 30
START_PLANTS = [ 'Tomato', 'Pumpkin', 'Watermelon' ]
START_FOOD = 0


def print_quit_dialogue(plants, day_count, food):
    """ Print the quit dialogue for the end of the simulation """
    if len(plants) == 0:
        print("You finished with no plants")
    else:
        print("you finished with these plants:")
        print(", ".join(str(plant) for plant in plants))

    print(f"After {day_count} days, you have {len(plants)} plants and your total food is {food}.")
    print("Thank you for simulating. Now go and enjoy a real garden.")


def add_new_plant(plants, food):
    """ Add new plants to plants list depending of food requirements """
    new_plant = input("Enter plant name: ").title()
    # Checks to see if plants are nor eligible or to expensive to be added to plants list
    if new_plant.isspace() or len(new_plant) == 0:
        print("Invalid Plant Name")
    elif new_plant.title() in plants:
        print("Plant Already Exists")
    elif food >= len(new_plant):
        food = food - len(new_plant)
        plants.append(new_plant)
    else:
        print(f"{new_plant} would cost {len(new_plant)} food. With only {food}, you can't afford it.")
    return plants, food


def wait_a_day(plants, food):
    """ Simulate waiting a day """
    if len(plants) != 0:
        rain_amount = random.randint(MIN_RAINFALL, MAX_RAINFALL)
        print(f"Rainfall: {rain_amount}mm")

        # Checks is plant should be deleted
        if rain_amount < LOW_RAINFALL_THRESHOLD:
            dead_plant = random.choice(plants)
            print(f"Sadly, your {dead_plant} plant has died.")
            plants.remove(dead_plant)

        # Lists all plants and food produced
        for plant in plants:
            food_rain_cast = random.randint(int(rain_amount/2), rain_amount)
            food_produced = int(food_rain_cast/100 * len(plant))
            food = food_produced + food
            print(f"{plant} produced {food_produced}", end=", ")
        print("\n")
    else:
        print("You have no plants left!")
        print("Buy more plants if you can or quit")

    return plants, food


def main():
    """ Main looping function """
    print(RAIN_ART)
    print(TITLE_TEXT)
    print(WELCOME)

    plants = START_PLANTS[ : ]
    print(*plants, sep=", ")

    food = START_FOOD

    day_count = 0
    while True:
        print("--------------------------------")
        print(f"After {day_count} days, you have {len(plants)} plants and your total food is {food}.")
        print(MENU)
        choice = input("Choose: ").upper()
        if choice == "W":
            day_count += 1
            plants, food = wait_a_day(plants, food)
        elif choice == "D":
            print(*plants, sep=", ")
        elif choice == "A":
            plants, food = add_new_plant(plants, food)
        elif choice == "Q":
            break
        else:
            print("Invalid choice")

    print_quit_dialogue(plants, day_count, food)


if __name__ == "__main__":
    main()
