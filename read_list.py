#-*- coding: cp1251 -*-
def main():
    infile = open('writeList.txt', 'r')
    test_list = infile.readlines()
    infile.close()
    indx = 0
    while indx < len(test_list):
        test_list[indx] = test_list[indx].rstrip('\n')
        indx += 1

    print(test_list)


if __name__ == '__main__':
    main()

