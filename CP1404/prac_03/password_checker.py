"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 4
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = get_password()
    print("Your {}-character password is valid: {}".format(len(password),
                                                           password))


def get_password():
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    return password


def is_valid_password(password):
    if not MAX_LENGTH > len(password) > MIN_LENGTH:
        return False

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0

    for char in password:
        if char.isdigit():
            count_digit += 1
        elif char.isupper():
            count_upper += 1
        elif char.islower():
            count_lower += 1
        elif char in SPECIAL_CHARACTERS:
            count_special += 1
        else:
            print("Error")
            return False

    if count_lower == 0 or count_digit == 0 or count_upper == 0:
        return False

    if SPECIAL_CHARS_REQUIRED:
        if count_special == 0:
            return False

    return True


main()