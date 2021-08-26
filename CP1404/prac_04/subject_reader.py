"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    display_data(data)


def display_data(data):
    for i in data:
        print(f"{i[0]}1 is taught by {i[1]}e and has {i[2]} students")


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    file_data = []
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")

        file_data.append(parts)

    input_file.close()

    return file_data


main()
