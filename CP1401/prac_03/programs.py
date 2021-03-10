# 1: Tax
def tax():
    # Pseudocode:
    # set TAX_RATE_LOW = 0.05
    # set TAX_RATE_HIGH = 0.1
    # set TAX_THRESHOLD_LOW = 100
    # set TAX_THRESHOLD_HIGH = 1000
    # get income
    # total_tax = 0
    # if income > TAX_THRESHOLD_HIGH:
    #     total_tax = income * TAX_RATE_HIGH
    # else if income >= TAX_THRESHOLD_LOW:
    #     total_tax = income * TAX_RATE_LOW
    # take_home_pay  = income - total_tax
    # display total_tax
    # display take_home_pay

    TAX_RATE_LOW = 0.05  # 5%set
    TAX_RATE_HIGH = 0.1  # 10%
    TAX_THRESHOLD_LOW = 100
    TAX_THRESHOLD_HIGH = 1000

    total_tax = 0

    print("Python Party Tax Program - Where Tax is a Party")
    income = float(input("Income: $"))

    if income > TAX_THRESHOLD_HIGH:
        total_tax = income * TAX_RATE_HIGH
    elif income >= TAX_THRESHOLD_LOW:
        total_tax = income * TAX_RATE_LOW

    take_home_pay  = income - total_tax

    print("Total tax is: $", round(total_tax, 2), sep="")
    print("Take home pay is: $", round(take_home_pay, 2), sep="")


# 2: Car Insurance
def car_insurance():
    REFUSE_HIRE = 18
    SPECIAL_INSURANCE = 25

    age = int(input("Age of renter: "))
    if age < REFUSE_HIRE:
         print("Hire refused")
    elif age < SPECIAL_INSURANCE:
         print("Insurance required")
    else:
        print("Insurance not required")


# 3: Simple Password Checker
def simple_password_checker():
    SECRET_PASSWORD = "Fancy Bear"

    input_password = input("Password: ")

    if input_password == SECRET_PASSWORD:
        print("Access granted")
    else:
        print("Access denied")


# 4: Dog Years
def dog_years_calculator():
    TWO_YEARS_HUMAN = 10.5
    NORMAL_DOG_YEAERS = 4

    human_years = int(input("Age in human years: "))
    if human_years >= 2:
        human_years = human_years - 2
        dog_years = TWO_YEARS_HUMAN
        dog_years = dog_years + NORMAL_DOG_YEAERS * human_years
    else:
        dog_years = human_years/2 * TWO_YEARS_HUMAN
    print(f"Age in dog years is {round(dog_years, 0)}")


# 5: Rock of Ages
def rock_of_ages():
    LOWER_RANGE = 0
    UPPER_RANGE = 120
    age = int(input("Age: "))
    if LOWER_RANGE < age < UPPER_RANGE:
        print("Valid age")
    else:
        print("Invalid age")
        print("Try Again")


# 6: Speeding Fines
def speeding_fines():
    # Less than 13km/h over the speed limit
    BELOW_13_SPEED = 13
    PENATLY_13 = 177
    DEMERIT_POINTS_13 = 1

    # At least 13km/h but not more than 20km/h over the speed limit
    INCLUSIVE_BELOW_20_SPEED = 20
    PENATLY_20 = 266
    DEMERIT_POINTS_20 = 3

    # More than 20km/h but not more than 30km/h over the speed limit
    INCLUSIVE_BELOW_30_SPEED = 30
    PENATLY_30 = 444
    DEMERIT_POINTS_30 = 4

    # More than 30km/h but not more than 40km/h over the speed limit
    INCLUSIVE_BELOW_40_SPEED = 40
    PENATLY_40 = 622
    DEMERIT_POINTS_40 = 6

    # More than 40km/h over the speed limit
    PENATLY_OVER_40 = 1245
    DEMERIT_POINTS_OVER_40 = 8

    users_speed = int(input("Users Speed: "))
    speed_limit = int(input("Speed Limit: "))

    speed_over = users_speed - speed_limit

    penalty_amount = 0
    demerit_points = 0
    if speed_over > 0:
        if speed_over < BELOW_13_SPEED:
            penalty_amount = PENATLY_13
            demerit_points = DEMERIT_POINTS_13
        elif speed_over <= INCLUSIVE_BELOW_20_SPEED:
            penalty_amount = PENATLY_20
            demerit_points = DEMERIT_POINTS_20
        elif speed_over <= INCLUSIVE_BELOW_30_SPEED:
            penalty_amount = PENATLY_30
            demerit_points = DEMERIT_POINTS_30
        elif speed_over <= INCLUSIVE_BELOW_40_SPEED:
            penalty_amount = PENATLY_40
            demerit_points = DEMERIT_POINTS_40
        else:
            penalty_amount = PENATLY_OVER_40
            demerit_points = DEMERIT_POINTS_OVER_40
    print(f"Your Penalty Amount is ${penalty_amount}")
    print(f"Demerit points Lost is {demerit_points}")



if __name__ == "__main__":
    tax()
    car_insurance()
    simple_password_checker()
    dog_years_calculator()
    rock_of_ages()
    speeding_fines()