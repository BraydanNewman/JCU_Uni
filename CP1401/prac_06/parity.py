def check_parity(number):
    return number % 2


def is_even(parity):
    if parity == 0:
        return "even"
    else:
        return "false"

def main():
    number = int(input("Input number: "))
    parity = check_parity(number)
    odd_even = is_even(parity)

    print(f"The number '{number}' is {odd_even}")


def test_parity():
    parity = check_parity(2)
    odd_even = is_even(parity)
    print(odd_even)

    parity = check_parity(3)
    odd_even = is_even(parity)
    print(odd_even)


if __name__ == '__main__':
    # test_parity()
    main()
