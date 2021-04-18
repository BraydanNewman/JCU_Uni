RISTRETTO_MAX = 2
NORMALE_MAX = 3


def get_valid_number(prompt, low, high):
    number = float(input(prompt))
    while number < low or number > high:
        print("Invalid input")
        number = float(input(prompt))
    return number


def determine_coffee_style(ratio):
    if ratio < RISTRETTO_MAX:
        return "Ristretto"
    elif ratio < NORMALE_MAX:
        return "Normale"
    else:
        return "Lungo"


def test_coffee():
    style = determine_coffee_style(1)
    print(style)  # This should be ristretto
    style = determine_coffee_style(2)
    print(style)  # This should be normale
    style = determine_coffee_style(13.5)
    print(style)  # This should be lungo


def main():
    coffee_dose = get_valid_number("Dose: ", 0, 100)
    coffee_yield = get_valid_number("Yield: ", 0, 100)
    ratio = coffee_yield / coffee_dose
    style = determine_coffee_style(ratio)
    print(f"1:{ratio :.1f} is considered {style}")

if __name__ == "__main__":
    # test_coffee()
    main()