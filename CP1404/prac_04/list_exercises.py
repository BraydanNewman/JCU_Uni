valid_usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']


def main():
    user_verification()
    numbers = []
    for i in range(5):
        numbers.append(input_sterilization("Number: "))
    print_facts(numbers)


def user_verification():
    username = input("Username: ")
    if username in valid_usernames:
        print("Access granted")
        return
    print("Access denied")
    exit()


def print_facts(numbers):
    print(f"The first number is {numbers[ 0 ]}")
    print(f"The last number is {numbers[ -1 ]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average number is {sum(numbers)/len(numbers)}")


def input_sterilization(prompt):
    while True:
        try:
            number = float(input(prompt))
        except ValueError:
            print("Input was not an Int or Float")
        else:
            return number


if __name__ == "__main__":
    main()
