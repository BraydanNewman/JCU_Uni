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
    # Wanted to avoid "MAGIC NUMBER" when doing the white coffee
    BLACK_COFFEE_COST = [3, 4, 5]
    WHITE_COFFEE_COST = [4, 5, 6]

    coffee_type = input("(B)lack or (W)hite Coffee: ").upper()
    size = input("Size - (S)mall, (M)edium or (L)arge").upper()

    if coffee_type == "B":
        if size == "S":
            pass
        elif size == "M":
            pass
        else:
            pass
    else:
        pass




if __name__ == "__main__":
    percentage_program()