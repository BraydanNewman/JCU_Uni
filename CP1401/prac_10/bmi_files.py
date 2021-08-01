FILE_NAME = 'bmis.txt'

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

def display_content(file_name):
    with open(file_name, "r") as txt_file:
        content = txt_file.readlines()
    for line in content:
        line = float(line.rstrip("\n"))
        print(f"BMI {line:.1f}, considered {determine_weight_category(line)}")

def main():
    people = int(input('Number of People: '))
    bmi_file = open(FILE_NAME, "w")
    for i in range(people):
        print(f'\nPerson {i + 1}')
        height = float(input("Height: "))
        weight = float(input("Weight: "))
        bmi_file.write(f"{str(calculate_bmi(height, weight))}\n")
    bmi_file.close()
    display_content(FILE_NAME)




if __name__ == '__main__':
    main()