import random

COFFEE_MENU = {
    "Flat White":
    """
Here's how to make a/n Flat White: 
- Insert portafilter into grinder
- Press grind button to grind beans into portafilter
- Distribute grounds
- Tamp grounds
- Insert full portafilter into group head
- Press shot button to pour espresso into cup
- Fill jug with milk
- Steam milk until nice microfoam formed and milk up to temperature
- Swirl milk gently in jug
- Pour milk into cup... carefully, artistically :)
        """,
    "Espresso":
    """
Here's how to make a/n Espresso: 
- Insert portafilter into grinder
- Press grind button to grind beans into portafilter
- Distribute grounds
- Tamp grounds
- Insert full portafilter into group head
- Press shot button to pour espresso into cup
    """,
    "Long Black":
    """
Here's how to make a/n Long Black: 
- Insert portafilter into grinder
- Press grind button to grind beans into portafilter
- Distribute grounds
- Tamp grounds
- Insert full portafilter into group head
- Press shot button to pour espresso into cup
- Add hot water to cup
    """,
    "Hot Chocolate":
    """
Dont be ridiculous, who doest know how to make a Hot Chocolate!!!!
        """
}

def coffee_shop():
    """ Simulate a coffee shop """
    print("Welcome to the IT@JCU Coffee Shop")

    drinkable_coffee = ""

    while True:
        print("(O)rder - (D)rink - (R)andom choice - (Q)uit")
        choice = input(">>> ").upper()
        if choice == "O":
            print("Please choice from:")
            print(f"{' - '.join(str(key) for key, value in COFFEE_MENU.items())}")
            while True:
                coffee_choice = input("? ").title()
                if coffee_choice in COFFEE_MENU:
                    drinkable_coffee = coffee_choice
                    print(COFFEE_MENU[coffee_choice])
                    break
                else:
                    print("Invalid Order")

        elif choice == "D":
            if drinkable_coffee == "":
                print("Oh... where's my coffee?")
            else:
                print(f"Mmmm, nice {drinkable_coffee}")
                drinkable_coffee = ""
        elif choice == "R":
            coffee_choice = random.choice(list(COFFEE_MENU.keys()))
            drinkable_coffee = coffee_choice
            print(COFFEE_MENU[coffee_choice])
        elif choice == "Q":
            print("Thanks for drinking coffee")
            break
        else:
            print("Invalid Choice")


def main():
    coffee_shop()


if __name__ == "__main__":
    main()
