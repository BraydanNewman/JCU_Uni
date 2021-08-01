DISCOUNT_BOUNDARY = 100
DISCOUNT_VALUE = 0.1

def main():
    num_items = int(input("Number of Items: "))
    total = 0
    for i in range(num_items):
        price = float(input("Price of items: "))
        total += price
    if total > DISCOUNT_BOUNDARY:
        total *= (1 - DISCOUNT_VALUE)
    print(f"Total price for {num_items} items is ${total:.2f}")

if __name__ == "__main__":
    main()
