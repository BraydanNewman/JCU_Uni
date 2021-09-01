"""
Replace the contents of this module docstring with your own details
Name: Braydan Newman
Date started: 30/08/2021
GitHub URL: https://github.com/BraydanNewman/uni_pracs/tree/master/CP1404
"""

import csv
import random
from operator import itemgetter

NAME_INDEX = 0
COUNTRY_INDEX = 1
PRIORITY_INDEX = 2
VISITED_INDEX = 3

VISITED_PREFIX = 'v'
UNVISITED_PREFIX = 'n'

CSV_FILENAME = 'places.csv'
MENU_ITEMS = """Menu:
L - List places 
R - Recommend random place 
A - Add new place 
M - Mark a place as visited 
Q - Quit """


def main():
    print("Travel Tracker 1.0 - by Braydan Newman")

    with open(CSV_FILENAME, 'r+', encoding='UTF8', newline="") as csv_file:
        places = convert_priority_to_int(list(csv.reader(csv_file)))
        csv_writer = csv.writer(csv_file)

        print(f"{len(places)} loaded from {CSV_FILENAME}")

        print(MENU_ITEMS)
        user_selection = input(">>> ").upper()
        while user_selection != "Q":
            if user_selection == "L":
                list_places(places)
            elif user_selection == "R":
                if total_unvisited_places(places) > 0:
                    recommend_random_place(places)
                else:
                    print(f"No places left to visit!")
            elif user_selection == "A":
                places = add_new_place(places)
            elif user_selection == "M":
                if total_unvisited_places(places) > 0:
                    list_places(places)
                    places = mark_place_visited(places)
                else:
                    print(f"No unvisited places")
            elif user_selection != "Q":
                print("Invalid menu choice")
            print(MENU_ITEMS)
            user_selection = input(">>> ").upper()
        print(f"{len(places)} places saved to {CSV_FILENAME}")
        print("Have a nice day :)")
        places = sort_places(places)
        csv_file.seek(0)
        csv_file.truncate()
        csv_writer.writerows(places)
    csv_file.close()


def input_int_type(prompt):
    """Get correct user input and convert to int above 0"""
    user_input = error_check_user_input(prompt).strip()
    input_error = True
    while input_error:
        if user_input.isdigit() and int(user_input) > 0:
            input_error = False
        else:
            print("please enter an integer above 0")
            user_input = error_check_user_input(prompt).strip()
    return int(user_input)


def add_new_place(places):
    """Add new place to places list"""
    name = error_check_user_input("Name: ")
    country = error_check_user_input("Country: ")
    priority = input_int_type("Priority: ")
    print(f"{name} in {country} (priority {priority}) added to Travel Tracker")
    places.append([name, country, priority, UNVISITED_PREFIX])
    return places


def error_check_user_input(prompt):
    """Check user input for being blank"""
    user_input = input(prompt)
    while user_input == "":
        if user_input != "":
            return user_input
        user_input = input(prompt)
        print("Input can not be blank")
    else:
        return user_input


def total_unvisited_places(places):
    """Count unvisited places"""
    count = 0
    for place in places:
        if place[VISITED_INDEX] == UNVISITED_PREFIX:
            count += 1
    return count


def mark_place_visited(places):
    """Change user selected place to visited"""
    places = sort_places(places)
    print("Enter the number of a place to mark as visited")
    input_error = True
    while input_error:
        user_selection = input(">>> ")
        try:
            user_selection = int(user_selection)
        except ValueError:
            print("Invalid input; enter a valid number")
        else:
            if user_selection > 0:
                if user_selection <= len(places):
                    if places[user_selection - 1][VISITED_INDEX] == UNVISITED_PREFIX:
                        place_in_csv_list = places.index(places[user_selection - 1])
                        places[place_in_csv_list][VISITED_INDEX] = VISITED_PREFIX
                        print(f"{places[user_selection - 1][NAME_INDEX]} in "
                              f"{places[user_selection - 1][COUNTRY_INDEX]} visited!")
                        return places
                    else:
                        print(f"You have already visited {places[user_selection - 1][NAME_INDEX]}")
                        return places
                else:
                    print("Invalid place number")
            else:
                print("Number must be > 0")


def recommend_random_place(places):
    """Recommend random place to user"""
    unvisited_place = [unvisited_place for unvisited_place in places
                       if unvisited_place[VISITED_INDEX] == UNVISITED_PREFIX]
    chosen_place = random.choice(unvisited_place)
    print("Not sure where to visit next?")
    print(f"How about... {chosen_place[NAME_INDEX]} in {chosen_place[COUNTRY_INDEX]}?")


def sort_places(places):
    """Sort and return list of places"""
    return sorted(places, key=itemgetter(VISITED_INDEX, PRIORITY_INDEX))


def length_of_longest_item(places, index):
    """Get length of longest item in list"""
    return len(max([str(row[index]) for row in places], key=len))


def list_places(places):
    """Display all places in list"""
    places = sort_places(places)
    unvisited_count = 0
    for index, item in enumerate(places):
        if item[VISITED_INDEX] == UNVISITED_PREFIX:
            visited_indicator = "*"
            unvisited_count += 1
        else:
            visited_indicator = ""
        print(f"{visited_indicator:1} {index + 1:{len(str(len(places)))}}. "
              f"{item[NAME_INDEX]:{length_of_longest_item(places, NAME_INDEX)}} in "
              f"{item[COUNTRY_INDEX]:{length_of_longest_item(places, COUNTRY_INDEX)}} "
              f"{item[PRIORITY_INDEX]:>{length_of_longest_item(places, PRIORITY_INDEX)}}")
    if unvisited_count == 0:
        print(f"{len(places)} places. No places left to visit. Why not add a new place?")
    else:
        print(f"{len(places)} places. You still want to visit {unvisited_count} places.")


def convert_priority_to_int(places):
    """Convert place priority to int type"""
    for i in range(len(places)):
        places[i][PRIORITY_INDEX] = int(places[i][PRIORITY_INDEX])
    return places


if __name__ == '__main__':
    main()
