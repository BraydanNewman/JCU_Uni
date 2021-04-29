import random


def calculate_minutes_and_seconds(time):
    minutes, seconds = divmod(time, 60)
    return minutes, seconds


def main():
    start = 0
    step = random.randint(1, 1000)
    reps = 5

    time = start
    for i in range(reps):
        minutes, seconds = calculate_minutes_and_seconds(time)
        print(f"{time} seconds is {minutes}m {seconds}s")
        time += step


if __name__ == '__main__':
    main()
