INSTRUCTIONS_STR = """
Enter the number of products you want to buy and your chosen price. 
If you buy 0-5 items, they're full price, over 5 
items and each one is 10% off!
"""

MENU_STR = """
Menu:
(I)nstructions
(C)alculate
(Q)uit
"""

PERCENT_10_OFF_THRESH_HOLD = 5

def main():
    while True:
        print(MENU_STR)
        choice = input("Choice: ").upper()

        if choice == "I":
            print(INSTRUCTIONS_STR)
        elif choice == "C":

            while True:
                num_products = int(input("Number of Products: "))
                if num_products >= 0:
                    break
                else:
                    print("Invalid Input")

            while True:
                price = int(input("Price: "))
                if price >= 0:
                    break
                else:
                    print("Invalid Input")

            total = num_products * price

            if num_products >= PERCENT_10_OFF_THRESH_HOLD:
                total = total - (total * 0.1)

            print(f"{num_products} x ${price} = ${total}")
        elif choice == "Q":
            break
        else:
            print("Invalid Input")


if __name__ == "__main__":
    main()