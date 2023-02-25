def main():


    # Получить список с хранящимися в нем значениями
    numbers = get_values()

    # Показать значения в списке.
    print('Значения в списке: ')
    print(numbers)


    # Функция get_values() получает от пользователя ряд значений
    # и сохраняет их в списке.
    # эта функция возвращает ССЫЛКУ на список.

def get_values():
    values = []
    again = 'y'
    while again == 'y':
        value = int(input('Введите значение от 1 до 10: '))
        values.append(value)
        again = input('Continue y/n: ')
        print()
    return values


if __name__ == '__main__':
    main()

