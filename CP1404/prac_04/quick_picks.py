import random

NUMBERS_IN_QUICK_PICK = 6
NUMBER_RANGE_MIN = 1
NUMBER_RANGE_MAX = 45


def main():
    rounds = input_sterilization("How many quick picks? ")
    for i in range(rounds):
        picks = []
        for j in range(NUMBERS_IN_QUICK_PICK):
            picks.append(random.randint(NUMBER_RANGE_MIN, NUMBER_RANGE_MAX))
        picks.sort()
        for number in picks:
            print(f"{number:3}", end='')
        print('')


def input_sterilization(prompt):
    while True:
        try:
            number = int(input(prompt))
        except ValueError:
            print("Input was not an Int or Float")
        else:
            return number


if __name__ == "__main__":
    main()
