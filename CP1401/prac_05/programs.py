# Percentage program (I, P, O)
# Time of day (Decisions)
# Coffee orders (Decisions)
# Coffee order error-checking (Repetitions)
# Low-high printing (Repetitions)


def percentage_program():
    original = float(input("Original value: "))
    change = float(input("Change value: "))

    print(f"Original: {original}, Change: {change}, Result: {(original * change) + original}")


def time_of_day():
    time = int(input("Time: "))
    if time < 12:
        output = ["before", "coming", "Hi"]
    else:
        output = ["after", "going", "Bye"]

    print(f"It is {output[0]} noon and you are {output[1]}. {output[2]}!")


def coffee_orders():
    # Cost goes small, medium, large in lists (that's just logical)
    BLACK_COFFEE_COST = [3, 4, 5]
    WHITE_COST_ADD = 1

    total = 0

    while True:
        coffee_type = input("(B)lack or (W)hite Coffee: ").upper()
        size = input("Size - (S)mall, (M)edium or (L)arge").upper()

        if size == "S":
            total = BLACK_COFFEE_COST[0]
        elif size == "M":
            total = BLACK_COFFEE_COST[1]
        elif size == "L":
            total = BLACK_COFFEE_COST[2]

        if coffee_type == "W" and total != 0:
            total += WHITE_COST_ADD
            break
        elif  coffee_type == "B":
            break

        print("Invalid Input(s)")

    print(f"Total: {total}")

def low_high_printing():
    number_1 = int(input("First number: "))
    number_2 = int(input("Second number: "))

    total = 0
    for i in range(number_1, number_2+1):
        total += i
        print(i, end=" ")
    print(f"totals: {total}")





if __name__ == "__main__":
    # percentage_program()
    # coffee_orders()
    low_high_printing()