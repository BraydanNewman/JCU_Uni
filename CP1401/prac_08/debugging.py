def friends_names():
    # Debug program 1 - friends' names

    # 1) 'range(1, len(names))' starts at 1 where as the index for the list starts at 0
    # 2) 'last_number = len(names)' is just getting the length and not accounting for the index stating at 0

    # names = ["Abby", "Jerome", "Olivia", "Monique"]
    # print("My friends' names: ")
    # for i in range(1, len(names)):
    #     print(f"{i}. {names[i]}")
    # last_number = len(names)
    # print(f"The last name is {names[last_number]}")

    names = ["Abby", "Jerome", "Olivia", "Monique"]
    print("My friends' names: ")
    for i in range(len(names)):
        print(f"{i + 1}. {names[i]}")
    last_number = len(names) - 1
    print(f"The last name is {names[last_number]}")

def title_casing_country_names():
    # Debug program 2 - title-casing country names

    # 'countries is a tuple and cant be modified
    # needs to be a list

    # countries = ("australia", "new zeaLAND", "USA")
    # for i in range(len(countries)):
    #     countries[ i ] = countries[ i ].title()

    countries = ["australia", "new zeaLAND", "USA"]
    for i in range(len(countries)):
        countries[i] = countries[i].title()


if __name__ == "__main__":
    friends_names()