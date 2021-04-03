# 1. Error Checking
def error_checking():
    SALARY_MULTIPLIER = 5000

    worker_level = float(input("What is your Worker level: "))
    while worker_level < 1 or worker_level > 10:
        print("Invalid worker level")
        worker_level = int(input("What is your Worker level: "))

    print(f"With worker level {worker_level}, your salary is ${round(worker_level*SALARY_MULTIPLIER, 2)}")


# 2. Number Sequences
def number_sequences():
    # A (odd numbers)
    for i in range(1, 101, 2):
        print(f"{i}\n")

    # B (Olympic years)
    for i in range(1896, 2021, 4):
        print(f"{i}\n")

    # C (i legit dont know)
    for i in range(333, 1000, 333):
        print(f"{i}\n")


# 3. Menus
# 4. Accumulation -- Smileys Count
def menus():
    menu_options = """
        -- (S)miley 
        -- (F)rowny 
        -- (Q)uit
    """

    total_smiles = 0
    total_frownies  = 0
    while True:
        print(menu_options)
        user_choice = input(">>>    ").upper()

        if user_choice == "S":
            total_smiles += 1
            print(":)")
        elif user_choice == "F":
            total_frownies += 1
            print(":(")
        elif user_choice == "Q":
            break
        else:
            print("Invalid choice")
    print("Farewell")
    print(f"Total smiles: {total_smiles}")
    print(f"Total frownies: {total_frownies}")


# 4. Accumulation -- Average Age
def average_age():
    SENTINEL = -1
    total_age = 0
    total_people = 0
    input_age = int(input("Age: "))
    while input_age != SENTINEL:
        total_age = total_age + input_age
        total_people += 1
        input_age = int(input("Age: "))
    print(f"Average age is {total_age/total_people:.2f}")


# 4. Accumulation -- Total Numbers
def total_numbers():
    number_loops = int(input("How many numbers do you want to add up? "))
    total_num = 0
    for i in range(number_loops):
        total_num += int(input(f"Enter number {i + 1}: "))
    print(f"The total of those {number_loops} numbers is {total_num}")


# 5. Guessing Game
def guessing_game():
    SECRET = 6
    guess = int(input("Guess a number: "))
    total_guesses = 1
    while guess != SECRET:
        if guess < SECRET:
            print("Higher")
        else:
            print("Lower")

        guess = int(input("Guess a number: "))
        total_guesses += 1
    print("You got it!")


# 6. Nested Loops
def nested_loops():
    row = int(input("Row: "))
    columns = int(input("Columns: "))

    for i in range(row):
        for j in range(columns):
            print(j, end =" ")
        print("")


if __name__ == '__main__':
    # error_checking()
    # number_sequences()
    # total_numbers()
    # menus()
    # guessing_game()
    nested_loops()