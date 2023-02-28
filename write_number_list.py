def main():

    numbers = [2, 4, 6, 8, 10]

    outfile = open('numberList.txt', 'w')

    for item in numbers:
        outfile.write(f'{item}\n')

    outfile.close()


if __name__ == '__main__':
    main()