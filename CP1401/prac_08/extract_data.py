RECORD = ["Jimmy", "Smith", (8, 12, 1928), "Piano"]


def main():
    print(f"Last name:  {RECORD[1]}")
    print(f"Born: {RECORD[2]}")
    print(f"{RECORD[0]} was born {RECORD[2]} and was a great {RECORD[3]} player")

if __name__ == "__main__":
    main()