from random import randint

def get_valid_number(prompt, min_number, max_number, error_message=None):
    while  True:
        number = int(input(prompt))
        if min_number <= number <= max_number:
            return number
        if error_message:
            print(error_message)


def random_num_gen(quantity, max_number):
    random_list = []
    for i in range(quantity):
        random_list.append(randint(0, max_number))
    return random_list


def reverse_list(random_list):
    return random_list[::-1]

def sort_list(random_list):
    return sorted(random_list, reverse=False)

def random_num_from_list(random_list):
    return random_list[randint(0, len(random_list) - 1)]


def print_answer(random_list):
    sorted_list= sort_list(random_list)
    random_num = random_num_from_list(random_list)
    reversed_list = reverse_list(random_list)
    
    print(f"The numbers are: {random_list}")
    print(f"The minimum is: {sorted_list[0]}")
    print(f"The maximum is: {sorted_list[len(sorted_list) - 1]}")
    print(f"A randomly chosen number is: {random_num}")
    print(f"The numbers reversed are: {reversed_list}")
    print(f"The numbers sorted are: {sorted_list}")


def main():
    quantity = get_valid_number("Number of random numbers: ", 1, 1000)
    max_number = get_valid_number("Maximum random number: ", 0, 1000000000)

    random_list = random_num_gen(quantity, max_number)
    print_answer(random_list)
    
    


if __name__ == '__main__':
    main()
