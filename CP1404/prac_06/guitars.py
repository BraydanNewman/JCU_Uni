from guitar import Guitar


def main():
    print("My guitars!")

    guitars = []
    name = input("Name: ")
    while name != "":
        year = input("Year: ")
        while not year.isdigit():
            print("Must be a number")
            year = input("Year: ")

        cost = input("Cost: ")

        guitars.append(Guitar(name, int(year), cost))
        print(f"{name} ({year}) : ${cost} added.")

        name = input("Name: ")

    length_of_longest_name = max([len(i.name) for i in guitars])

    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar.name:{length_of_longest_name}} "
              f"({guitar.year}), worth $ {guitar.cost} {'(vintage)' if guitar.is_vintage() else ''}")


if __name__ == "__main__":
    main()
