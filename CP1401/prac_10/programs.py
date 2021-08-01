# 1. Read a String from a File
def read_a_string_from_a_file():
    in_file = open("name.txt", "r")
    text = in_file.read().strip()
    print(text)

def write_numbers_to_a_file():
    with open('range.txt', 'w') as out_file:

        # for i in range(0, 99, 2):
        #     out_file.write(str(i) + "\n")
        #
        # for i in range(0, 100, 10):
        #     out_file.write(str(i) + "\n")

        for i in range(20, 0, -1):
            out_file.write(str(i) + "\n")

def greater_than_counter():
    filename = input("Filename: ")
    threshold = float(input("Threshold: "))
    print("Processing...")
    with open(filename, 'r') as in_file:
        file_data = in_file.readlines()
    count = 0
    for num in file_data:
        if float(num.rstrip("\n")) > threshold:
            count += 1
    print(f'{count} out of {len(file_data)} ({(count/len(file_data))*100}%) values in {filename} are greater than {threshold}.')





def main():
    # read_a_string_from_a_file()
    # write_numbers_to_a_file()
    greater_than_counter()

if __name__ == '__main__':
    main()
