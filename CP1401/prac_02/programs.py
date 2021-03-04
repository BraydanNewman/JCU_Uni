def discount_price():
    original_price = int(input("Original Price: "))
    discount = original_price * 0.2
    new_price = original_price - discount
    print(f"New Price: {new_price}")


def kilometres_to_miles():
    distances_km = int(input("Distance in Kilometers: "))
    distances_mi = distances_km * 0.62137
    print(f"Distance in Miles: {distances_mi}")


def holiday_cost():
    food_cost = int(input("Daily food cost: $"))
    activity_cost = int(input("Daily activities cost: $"))
    num_day = int(input("Number Of Days: "))
    total = (food_cost + activity_cost) * num_day
    print(f"Total holiday cost: {total}")


def i_stop_calculation():
    i_stop_on = int(input("i-stop on in seconds: "))
    time_stopped = int(input("Time stopped in seconds: "))

    percentage = round((i_stop_on / time_stopped) * 100, 1)

    print(f"i-stop ON: {i_stop_on // 60}m {i_stop_on % 60}s")
    print(f"Time Stopped: {time_stopped // 60}m {time_stopped % 60}s")
    print(f"Percentage: {percentage}%")


def bmi_calculator():
    height = int(input("Height: "))
    weight = int(input("Weight: "))
    bmi = round((weight / (height ** 2)) * 10000, 1)
    print(f"BMI: {bmi}")


def number_conversion():
    print("1) Kilograms to pounds")
    print("2) Pounds to Kilograms")
    print("3) Fahrenheit to Celsius")
    print("4) Celsius to Fahrenheit")
    choice = int(input('Choice: '))
    print("")

    if choice == 1:
        kilograms = int(input("Kilograms: "))
        print(f"{kilograms} kilograms is {round(kilograms*2.205, 2)} pounds")
    elif choice == 2:
        pounds = int(input("Pounds: "))
        print(f"{pounds} pounds is {round(pounds / 2.205, 2)} kilograms")
    elif choice == 3:
        fahrenheit = int(input("Fahrenheit: "))
        celsius  = (fahrenheit - 32.0) * 5.0 / 9.0
        print(f"{fahrenheit} degrees fahrenheit is {round(celsius, 2)} degrees celsius")
    elif choice == 4:
        celsius = int(input("Celsius: "))
        fahrenheit = (celsius * 9.0 / 5.0) + 32.0
        print(f"{celsius} degrees celsius is {round(fahrenheit, 2)} degrees fahrenheit")
    else:
        print("Not a valid input, please chose again")
        print("")
        number_conversion()



if __name__ == "__main__":
    # Uncomment the function you'd like to use

    # discount_price()
    # kilometres_to_miles()
    # holiday_cost()
    # i_stop_calculation()
    # bmi_calculator()
    number_conversion()

