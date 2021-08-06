finished = False
result = 0
while not finished:
    try:
        result = int(input(">>> "))
    except:
        print("Please enter a valid integer.")
    else:
        finished = True
print("Valid result is: ", result)
