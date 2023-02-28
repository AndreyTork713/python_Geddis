def main():

    infile = open('numberList.txt', 'r')

    numbers = infile.readlines()
    print(numbers)

    index = 0
    while index < len(numbers):
        numbers[index] = int(numbers[index])
        index += 1
    print(numbers)


if __name__ == '__main__':
    main()
