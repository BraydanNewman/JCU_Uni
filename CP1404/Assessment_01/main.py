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
    csv_list = list(read_as_csv(plain_file))

    print(f"{len(csv_list)} loaded from {CSV_FILENAME}")

    while True:
        print(MENU_ITEMS)
        user_selection = input(">>> ").upper()
        if user_selection == "L":
            list_places(csv_list)
        elif user_selection == "R":
            if num_of_unvisited_places(csv_list) > 0:
                recommend_random_place(csv_list)
            else:
                print(f"No places left to visit!")
        elif user_selection == "A":
            csv_list = add_new_place(csv_list)
        elif user_selection == "M":
            if num_of_unvisited_places(csv_list) > 0:
                list_places(csv_list)
                csv_list = mark_place_visited(csv_list)
            else:
                print(f"No unvisited places")
        elif user_selection == "Q":
            break
        else:
            print("Invalid menu choice")


def add_new_place(csv_list):
    name = error_check_user_input("Name: ")
    country = error_check_user_input("Country: ")
    priority = error_check_user_input("Priority: ")

    print(f"{name} in {country} (priority {priority}) added to Travel Tracker")

    csv_list.append([name, country, priority, "v"])
    return csv_list


def error_check_user_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input != "":
            return user_input
        print("Input can not be blank")


def num_of_unvisited_places(csv_list):
    count = 0
    for place in csv_list:
        if place[VISITED_INDEX] == "n":
            count += 1
    return count


def mark_place_visited(csv_list):
    sorted_csv = sort_places(csv_list)
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
            place_in_csv_list = csv_list.index(sorted_csv[user_selection - 1])
            csv_list[place_in_csv_list][VISITED_INDEX] = "v"
            print(f"{sorted_csv[user_selection - 1][NAME_INDEX]} in "
                  f"{sorted_csv[user_selection - 1][COUNTRY_INDEX]} visited!")
            return csv_list
        else:
            print(f"You have already visited {sorted_csv[user_selection - 1][NAME_INDEX]}")
            return csv_list


def recommend_random_place(csv_list):
    unvisited_place = [unvisited_place for unvisited_place in csv_list if unvisited_place[VISITED_INDEX] == "n"]
    chosen_place = random.choice(unvisited_place)
    print("Not sure where to visit next?")
    print(f"How about... {chosen_place[NAME_INDEX]} in {chosen_place[COUNTRY_INDEX]}?")


def sort_places(csv_list):
    visited_locations = []
    unvisited_locations = []

    for location in csv_list:
        if location[VISITED_INDEX] == VISITED_PREFIX:
            visited_locations.append(location)
        else:
            unvisited_locations.append(location)

    visited_locations.sort(key=itemgetter(2))
    unvisited_locations.sort(key=itemgetter(2), reverse=True)

    return unvisited_locations + visited_locations


def get_single_column(csv_list, index):
    return [row[index] for row in csv_list]


def length_of_longest_item(csv_list, index):
    return len(max(get_single_column(csv_list, index), key=len))


def list_places(csv_list):
    sorted_csv = sort_places(csv_list)
    unvisited_count = 0
    for index, item in enumerate(sorted_csv):
        if item[VISITED_INDEX] == 'n':
            visited_visual = "*"
            unvisited_count += 1
        else:
            visited_visual = ""
        print(f"{visited_visual:1} {index + 1:{len(str(len(csv_list)))}}. "
              f"{item[NAME_INDEX]:{length_of_longest_item(csv_list, NAME_INDEX)}} in "
              f"{item[COUNTRY_INDEX]:{length_of_longest_item(csv_list, COUNTRY_INDEX)}} "
              f"{item[PRIORITY_INDEX]:>{length_of_longest_item(csv_list, PRIORITY_INDEX)}}")
    if unvisited_count == 0:
        print(f"{len(csv_list)} places. No places left to visit. Why not add a new place?")
    else:
        print(f"{len(csv_list)} places. You still want to visit {unvisited_count} places.")


def open_file(filename):
    return open(filename, "r")


def read_as_csv(file_object):
    return csv.reader(file_object)


def close_file(filename):
    filename.close()


if __name__ == '__main__':
    main()
