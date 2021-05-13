import random

RAIN_ART = """
                             000      00
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
        / / / / / / / / / /
"""

TITLE_TEXT = """
  __  __             _         _      ___                _              ___  _              _        _             
 |  \/  | __ _  _ _ | |__ ___ | |_   / __| __ _  _ _  __| | ___  _ _   / __|(_) _ __  _  _ | | __ _ | |_  ___  _ _ 
 | |\/| |/ _` || '_|| / // -_)|  _| | (_ |/ _` || '_|/ _` |/ -_)| ' \  \__ \| || '  \| || || |/ _` ||  _|/ _ \| '_|
 |_|  |_|\__,_||_|  |_\_\\___| \__|  \___|\__,_||_|  \__,_|\___||_||_| |___/|_||_|_|_|\_,_||_|\__,_| \__|\___/|_|  
 
"""

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


def get_valid_number(prompt, min_number, max_number, error_message=None):
    while True:
        number = float(input(prompt))
        if min_number <= number <= max_number:
            return number
        if error_message:
            print(error_message)


def print_quit_dialogue(plants, day_count, food):
    print(f"""
You finished with these plants:
{", ".join(str(plant) for plant in plants)},
After {day_count} days, you have {len(plants)} plants and your total food is {food}.
Thank you for simulating. Now go and enjoy a real garden.
    """)


def add_new_plant(plants, food):
    new_plant = input("Enter plant name: ").title()
    if new_plant.isspace() or len(new_plant) == 0:
        print("Invalid Plant Name")
        return plants, food
    if new_plant.title() in plants:
        print("Plant Already Exists")
        return plants, food
    if food >= len(new_plant):
        food = food - len(new_plant)
        plants.append(new_plant)
    else:
        print(f"{new_plant} would cost {len(new_plant)} food. With only {food}, you can't afford it.")
    return plants, food


def wait_a_day(plants, food):
    rain_amount = random.randint(MIN_RAINFALL, MAX_RAINFALL)
    print(f"Rainfall: {rain_amount}mm")

    if rain_amount < LOW_RAINFALL_THRESHOLD:
        dead_plant = random.choice(plants)
        print(f"Sadly, your {dead_plant} plant has died.")
        plants.remove(dead_plant)
    
    for plant in plants:
        food_rain_cast = random.randint(int(rain_amount/2), rain_amount)
        food_produced = int(food_rain_cast/100 * len(plant))
        food = food_produced + food
        print(f"{plant} produced {food_produced}", end=", ")
    print("\n")

    return plants, food

    # Rainfall: 74mm
    # Parsley produced 3, Sage produced 1, Rosemary produced 3, Thyme produced 2,


def main():
    print(WELCOME)

    plants = START_PLANTS[ : ]
    print(*plants, sep=", ")

    food = START_FOOD

    day_count = 0
    while len(plants) > 1:
        while True:
            print("--------------------------------")
            print(f"After {day_count} days, you have {len(plants)} plants and your total food is {food}.")
            print(MENU)
            choice = input("Choose: ").upper()
            if choice == "W":
                day_count += 1
                plants, food = wait_a_day(plants, food)
                break
            elif choice == "D":
                print(*plants, sep=", ")
                break
            elif choice == "A":
                plants, food = add_new_plant(plants, food)
                break
            elif choice == "Q":
                print_quit_dialogue(plants, day_count, food)
                exit()
            else:
                print("Invalid choice")


if __name__ == "__main__":
    print(RAIN_ART)
    print(TITLE_TEXT)
    main()
