"""
Replace the contents of this module docstring with your own details
Name: Braydan Newman
Date started: 30/08/2021
GitHub URL: https://github.com/BraydanNewman/uni_pracs/tree/master/CP1404
"""

import csv
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

    list_places(csv_list)

    # while True:
    #     print(MENU_ITEMS)
    #     break


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
    for index, item in enumerate(sorted_csv):
        if item[VISITED_INDEX] == 'n':
            visited_visual = "*"
        else:
            visited_visual = ""
        print(f"{visited_visual:1} {index:{len(str(len(csv_list)))}}. "
              f"{item[NAME_INDEX]:{length_of_longest_item(csv_list, NAME_INDEX)}} in "
              f"{item[COUNTRY_INDEX]:{length_of_longest_item(csv_list, COUNTRY_INDEX)}}")


def open_file(filename):
    return open(filename, "r")


def read_as_csv(file_object):
    return csv.reader(file_object)


def close_file(filename):
    filename.close()


if __name__ == '__main__':
    main()
