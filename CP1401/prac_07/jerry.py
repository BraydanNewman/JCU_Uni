# Less than 13km/h over the speed limit
BELOW_13_SPEED = 13
PENALTY_13 = 177

# At least 13km/h but not more than 20km/h over the speed limit
INCLUSIVE_BELOW_20_SPEED = 20
PENALTY_20 = 266

# More than 20km/h but not more than 30km/h over the speed limit
INCLUSIVE_BELOW_30_SPEED = 30
PENALTY_30 = 444

# More than 30km/h but not more than 40km/h over the speed limit
INCLUSIVE_BELOW_40_SPEED = 40
PENALTY_40 = 622

# More than 40km/h over the speed limit
PENALTY_OVER_40 = 1245

def get_valid_number(prompt, min_number, max_number, error_message=None):
    while True:
        number = int(input(prompt))
        if min_number <= number <= max_number:
            return number
        if error_message:
            print(error_message)

def mph_to_kph(distances_mph):
    distances_kmh = distances_mph * 1.609344
    return distances_kmh


def speeding_fines(users_speed, speed_limit):
    speed_over = users_speed - speed_limit

    penalty_amount = 0
    if speed_over > 0:
        if speed_over < BELOW_13_SPEED:
            penalty_amount = PENALTY_13
        elif speed_over <= INCLUSIVE_BELOW_20_SPEED:
            penalty_amount = PENALTY_20
        elif speed_over <= INCLUSIVE_BELOW_30_SPEED:
            penalty_amount = PENALTY_30
        elif speed_over <= INCLUSIVE_BELOW_40_SPEED:
            penalty_amount = PENALTY_40
        else:
            penalty_amount = PENALTY_OVER_40

    print(f"Your fine is {penalty_amount}")

    return penalty_amount


def calculate_bank_balance_after_fine(bank_balance, fine):
    return bank_balance - fine


def main():
    speed_in_mph = get_valid_number("Speed in MPH: ", 0, 300, "Invalid speed")
    speed_in_kph = mph_to_kph(speed_in_mph)
    speed_limit_in_kph = get_valid_number("Speed limit in km/h: ", 0, 150, "Invalid speed limit")
    bank_balance = get_valid_number("Bank balance: ", 0, 100000000000000000, "Invalid Number")
    penalty_amount = speeding_fines(speed_in_kph, speed_limit_in_kph)
    bank_balance_after_fine = calculate_bank_balance_after_fine(bank_balance, penalty_amount)
    print(f"Your bank Balance after your fine will be {bank_balance_after_fine}")


if __name__ == '__main__':
    main()
