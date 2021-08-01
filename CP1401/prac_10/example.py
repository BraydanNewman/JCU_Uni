total = 0.0
count = 0
in_file = input("File name: ")
in_file = open(in_file, 'r')
for line in in_file:
    score = float(line)
    total += score
    print(f"Score = {score:4.1f}   Total so far =   {total:4.1f}")
    count += 1
in_file.close()
average = total / count
print(f"Average = {average:.1f}")
