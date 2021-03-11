choice = input("Steak choice (rare, medium or well-done): ").lower()
if choice == "rare":
    print("2 minutes")
elif choice == "medium":
    print("4 minutes")
elif choice == "well-done":
    print("6 minutes")
elif choice == "burnt":
    print("8 minutes")
else:
    print("Ain't no steak like that here")