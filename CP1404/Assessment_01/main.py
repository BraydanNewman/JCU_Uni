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

CSV_FILENAME = 'places.csv'
MENU_ITEMS = """Menu:
L - List places 
R - Recommend random place 
A - Add new place 
M - Mark a place as visited 
Q - Quit """


def main():
    print("Travel Tracker 1.0 - by Braydan Newman")

    plain_file = open_file(CSV_FILENAME)
    places = read_as_csv(plain_file)

    print(f"{len(places)} loaded from {CSV_FILENAME}")

    while True:
        print(MENU_ITEMS)
        user_selection = input(">>> ").upper()
        if user_selection == "L":
            list_places(places)
        elif user_selection == "R":
            if num_of_unvisited_places(places) > 0:
                recommend_random_place(places)
            else:
                print(f"No places left to visit!")
        elif user_selection == "A":
            places = add_new_place(places)
        elif user_selection == "M":
            if num_of_unvisited_places(places) > 0:
                list_places(places)
                places = mark_place_visited(places)
            else:
                print(f"No unvisited places")
        elif user_selection == "Q":
            break
        else:
            print("Invalid menu choice")


def add_new_place(places):
    name = error_check_user_input("Name: ")
    country = error_check_user_input("Country: ")
    priority = error_check_user_input("Priority: ")


    print(f"{name} in {country} (priority {priority}) added to Travel Tracker")

    places.append([name, country, priority, "v"])
    return places


def error_check_user_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input != "":
            return user_input
        print("Input can not be blank")


def num_of_unvisited_places(places):
    count = 0
    for place in places:
        if place[VISITED_INDEX] == "n":
            count += 1
    return count


def mark_place_visited(places):
    sorted_csv = sort_places(places)
    print("Enter the number of a place to mark as visited")
    while True:
        user_selection = input(">>> ")
        try:
            user_selection = int(user_selection)
        except ValueError:
            print("Invalid input; enter a valid number")
            continue
        if user_selection <= 0:
            print("Number must be > 0")
            continue
        if user_selection > len(sorted_csv):
            print("Invalid place number")
            continue
        if sorted_csv[user_selection - 1][VISITED_INDEX] == "n":
            place_in_csv_list = places.index(sorted_csv[ user_selection - 1 ])
            places[place_in_csv_list ][VISITED_INDEX ] = "v"
            print(f"{sorted_csv[user_selection - 1][NAME_INDEX]} in "
                  f"{sorted_csv[user_selection - 1][COUNTRY_INDEX]} visited!")
            return places
        else:
            print(f"You have already visited {sorted_csv[user_selection - 1][NAME_INDEX]}")
            return places


def recommend_random_place(places):
    unvisited_place = [ unvisited_place for unvisited_place in places if unvisited_place[VISITED_INDEX ] == "n" ]
    chosen_place = random.choice(unvisited_place)
    print("Not sure where to visit next?")
    print(f"How about... {chosen_place[NAME_INDEX]} in {chosen_place[COUNTRY_INDEX]}?")


def sort_places(places):
    return sorted(places, key=itemgetter(3, 2))


def length_of_longest_item(places, index):
    return len(max([ str(row[index]) for row in places ], key=len))


def list_places(places):
    sorted_csv = sort_places(places)
    unvisited_count = 0
    for index, item in enumerate(sorted_csv):
        if item[VISITED_INDEX] == 'n':
            visited_visual = "*"
            unvisited_count += 1
        else:
            visited_visual = ""
        print(f"{visited_visual:1} {index + 1:{len(str(len(places)))}}. "
              f"{item[NAME_INDEX]:{length_of_longest_item(places, NAME_INDEX)}} in "
              f"{item[COUNTRY_INDEX]:{length_of_longest_item(places, COUNTRY_INDEX)}} "
              f"{item[PRIORITY_INDEX]:>{length_of_longest_item(places, PRIORITY_INDEX)}}")
    if unvisited_count == 0:
        print(f"{len(places)} places. No places left to visit. Why not add a new place?")
    else:
        print(f"{len(places)} places. You still want to visit {unvisited_count} places.")


def open_file(filename):
    return open(filename, "r")


def read_as_csv(file_object):
    places = list(csv.reader(file_object))
    for i in range(len(places)):
        places[i][PRIORITY_INDEX] = int(places[i][PRIORITY_INDEX])
    return places


def close_file(filename):
    filename.close()


if __name__ == '__main__':
    main()
