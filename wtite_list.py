def main():
    test_list = ['Новосибирск', 'Омск', 'Томск', 'Красноярск']
    outfile = open('writeList.txt', 'w')
    for item in test_list:
        outfile.write(item + '\n')
    outfile.close()
    print('Данные записаны в файл writeList.txt')


if __name__ == '__main__':
    main()