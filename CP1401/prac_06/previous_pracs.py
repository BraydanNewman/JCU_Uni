SALARY_MULTIPLIER = 5000
WORKER_LEVEL_MIN = 1
WORKER_LEVE_MAX = 10


def get_valid_number(prompt, min_number, max_number, error_message=None):
    while  True:
        number = int(input(prompt))
        if min_number <= number <= max_number:
            return number
        if error_message:
            print(error_message)


def print_grid(row, columns):
    for i in range(row):
        for j in range(columns):
            print(j, end=" ")
        print("")


def calculate_salary(worker_level):
    return round(worker_level * SALARY_MULTIPLIER, 2)


def main():
    choice = get_valid_number("Type (1) to calculate salary or type (2) to print grid: ", 1, 2, "Invalid choice")
    if choice == 1:
        worker_level = get_valid_number("What is your Worker level: ",
                                        WORKER_LEVEL_MIN,
                                        WORKER_LEVE_MAX,
                                        "Invalid worker level")
        pay = calculate_salary(worker_level)
        print(f"With worker level {worker_level}, your salary is ${ pay }")
    else:
        row = get_valid_number("Rows: ", 1, 20, "Invalid choice")
        columns = get_valid_number("Columns: ", 1, 20, "Invalid choice")
        print_grid(row, columns)
    


if __name__ == '__main__':
    main()