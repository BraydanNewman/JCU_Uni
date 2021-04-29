def calculate_bmi(height, weight):
    return weight / (height ** 2)


def determine_weight_category(bmi):
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "normal"
    elif bmi < 30:
        return "overweight"
    else:
        return "obese"

def main():
    start_height = 150
    step_height = 10
    max_height = 200

    start_weight = 50
    step_weight = 10
    max_weight = 110

    for height in range(start_height, max_height, step_height):
        for weight in range(start_weight, max_weight, step_weight):
            bmi = calculate_bmi(height/100, weight)
            category = determine_weight_category(bmi)
            print(f"Height {height/100:.2f}m, Weight {weight:3}kg = BMI {bmi:.1f}, considered {category}")

if __name__ == '__main__':
    main()
