def calculate_human_to_dog_years(human_years):
    if human_years <= 2:
        return human_years * 10.5
    else:
        return 21 + 4 * (human_years - 2)

def main():
    while True:
        human_years = int(input("Age in human years: "))
        if human_years < 0:
            print("Exit")
            break
        print(calculate_human_to_dog_years(human_years))

if __name__ == '__main__':
    main()
