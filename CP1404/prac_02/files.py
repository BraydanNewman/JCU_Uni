# 1
name = input(">>> ")
with open('name.txt', 'w') as f:
    f.write(name)

# 2
with open('name.txt', 'r') as f:
    print(f"Your name is {f.readline()}")

# 3
with open('numbers.txt', 'r') as f:
    num1 = int(f.readline())
    num2 = int(f.readline())
    print(num1 + num2)

# 4
with open('numbers.txt', 'r') as f:
    num_list = f.readlines()
    total = 0
    for i in num_list:
        total += int(i.strip('\n'))
    print(total)
