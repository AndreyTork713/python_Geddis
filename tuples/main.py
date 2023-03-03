# КОРТЕЖИ
def main():
    my_tuple = (1, 2, 3, 4, 5)
    print(my_tuple)

    names = ('Holly', 'Yorren', 'Eshly')
    for n in names:
        print(n)
    print()
    for i in range(len(names)):
        print(names[i])
    print()
    # кортеж с одним элементом
    one_element = (1,)
    print(one_element)
    print()

    number_tuple = (1, 2, 3, 4, 5)
    print(number_tuple)
    number_list = list(number_tuple)
    print(number_list)
    print()

    string_tuple = ('dfdddfj', 'emgikred', 'fewer9ie')
    print(string_tuple)
    string_list = list(string_tuple)
    print(string_list)


if __name__ == '__main__':
    main()

