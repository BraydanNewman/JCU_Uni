places = []
longest_place = ""
place = input("Place: ").title()
while place != "":
    if len(longest_place) < len(place):
        longest_place = place
    places.append(place)
    place = input("Place: ")
if len(places) != 0:
    print("On my holiday, I went to: ")
    for place in places:
        if place != longest_place:
            print(place)
    print(f"The place with the longest name was '{longest_place}'")
else:
    print("I went nowhere :(")