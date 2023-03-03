def main():

    # Очередное освоение GITHUB

    list1 = [1, 2, 3, 4]
    list2 = []
    for item in list1:
        list2.append(item)
    print(f'list1: {list1}')
    print(f'list2: {list2}')
    print()
    list_1 = [11, 21, 31, 41]
    list_2 = [item ** 2 for item in list_1]
    list_3 = [item ** 2 for item in list_1 if item < 30]

    print(f'list_1: {list_1}')
    print(f'list_2: {list_2}')
    print(f'list_3: {list_3}')

    print()
    list_11 = ['eegjg', 'gfjede', 'gclgvmf', 'fdx;sfd', 'dfirjggr']
    list_21 = [item for item in list_11]
    list_31 = [item for item in list_11 if len(item) < 7]

    print(f'list_11: {list_11}')
    print(f'list_21: {list_21}')
    print(f'list_31: {list_31}')


if __name__ == '__main__':
    main()