def check(string, sub_str):
    if string.find(sub_str) == -1:
        return False
    else:
        return True

def main():
    input_file_name = input("Input file name: ")
    output_file_name = input("Output file name: ")
    search = input("Search String: ")

    output_file = open(output_file_name, "w")

    with open(input_file_name, 'r') as input_file:
        for line in input_file:
            if check(line, search):
                output_file.write(line)

    output_file.close()

if __name__ == "__main__":
    main()
