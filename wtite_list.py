#-*- coding: cp1251 -*- # ������������ ���������
def main():
    test_list = ['�����������', '����', '�����', '����������']
    outfile = open('writeList.txt', 'w')
    for item in test_list:
        outfile.write(item + '\n')
    outfile.close()
    print('������ �������� � ���� writeList.txt')


if __name__ == '__main__':
    main()