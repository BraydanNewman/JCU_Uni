from guitar import Guitar


def main():
    test_guitar = Guitar("Gibson L-5 CES", 1922, 16035)

    print(f"{test_guitar.name} get_age() - Expected 99 got {test_guitar.get_age()}")
    print(f"{test_guitar.name} is_vintage() - Expected True got {test_guitar.is_vintage()}")


if __name__ == "__main__":
    main()
