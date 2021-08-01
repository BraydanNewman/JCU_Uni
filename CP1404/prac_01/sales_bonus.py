"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

LOW_BONUS = 0.1
HIGH_BONUS = 0.15
BONUS_BOUNDARY = 1000

def main():
    while True:
        sales = int(input("Enter sales: $"))
        if sales < 0:
            break
        else:
            if sales < BONUS_BOUNDARY:
                print(f"Bonus: ${sales * LOW_BONUS}")
            else:
                print(f"Bonus: ${sales * HIGH_BONUS}")



if __name__ == "__main__":
    main()
