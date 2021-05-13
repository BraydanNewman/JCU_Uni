YEAR_STRING = {
    1: "first-year",
    2: "second-year",
    3: "third-year",
    4: "fourth-year",
    5: "Masters or other"
}

def print_hyphens(amount=40):
    """ Print a specified amount of hyphens (Default = 40) """
    for _ in range(amount):
        print('-', end="")
    print("\n")

def odd_or_even(num: int):
    """ Determine if int is 'Even' or 'Odd' """
    if num%2 == 0:
        return "Even"
    else:
        return "Odd"


def non_empty_str():
    """ Ask for users name and birthplace and returns is not empty """
    def empty_str_check(input_string):
        if input_string.isspace() or len(input_string) == 0:
            return True
        else:
            return False

    while True:
        name = input("What is your name: ").title()
        if empty_str_check(name):
            print("Try again")
        else:
            break
    while True:
        birthplace = input("Where were you born: ").title()
        if empty_str_check(birthplace):
            print("Try again")
        else:
            break
    return  name, birthplace

def number_list():
    """ Generate list of numbers between a max and min """
    min_num = int(input("Minimum number: "))
    while True:
        max_num = int(input("Maximum number: "))
        if min_num >= max_num:
            print(f"Your maximum must be greater than {min_num}")
        else:
            break
    complete_num_list = []
    for i in range(min_num, max_num + 1):
        complete_num_list.append(i)
    print(complete_num_list)

def subject_list():
    """ Ask user subject codes and displays them """
    complete_subject_codes = []
    while True:
        subject_code = input("Enter subject code: ").upper()
        if subject_code == "":
            break
        if subject_code[:2].isalpha() and subject_code[2:].isdigit() and len(subject_code) == 6:
            complete_subject_codes.append(subject_code)
        else:
            print("Invalid subject code")

    print(f"You do these {len(complete_subject_codes)} subjects: ")
    for code in complete_subject_codes:
        print(code)
    if "CP1401" in complete_subject_codes:
        print("You are cool")


def processing_string():
    """ Get data values from data_strings """
    data_strings = [ "Result = 95%", "Final Score = 8%", "Relative Value = 178%",
                     "Something else that's very important = 9.2%", "x = 42%" ]
    for i in data_strings:
        print(float(i.split(" = ")[1].strip("%")))

def subject_code_string():
    """ Display information about subject code """
    while True:
        subject_code = input("Enter subject code: ").upper()
        if subject_code == "":
            break
        if subject_code[:2].isalpha() and subject_code[2:].isdigit() and len(subject_code) == 6:
            print(f"That is a {YEAR_STRING[int(subject_code[2])]}{ ' IT' if subject_code[:2] == 'CP' else '' } subject.")
        else:
            print("Invalid subject code")


def main():
    print_hyphens()

    print(odd_or_even(32))

    name, birthplace = non_empty_str()
    print(f"Hi {name} from {birthplace}!")

    number_list()

    subject_list()

    processing_string()

    subject_code_string()


if __name__ == "__main__":
    main()