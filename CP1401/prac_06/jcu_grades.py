import random

MAX_SCORE = 100

def get_valid_number(prompt, min_number, max_number):
    while  True:
        score = int(input(prompt))
        if min_number <= score <= max_number:
            return score
        elif score < 0:
            get_random_scores()


def get_random_scores():
    loop_times = abs(int(input("How many random scores: ")))
    for _ in range(loop_times):
        main(random.randint(0, MAX_SCORE))
    exit()


def calculate_grade(score):
    if score >= 86:
        return "HD"
    elif score >= 60:
        return "D"
    elif score >= 40:
        return "P"
    else:
        return "N"

def main(score=None):
    if score is None:
        score = get_valid_number("Score: ", 0, MAX_SCORE)
    grade = calculate_grade(score)

    print(f"{score} = {grade}")


if __name__ == '__main__':
    main()