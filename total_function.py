def main():
    # Создать список
    numbers = [2, 4, 6, 8, 10]

    def get_total(numbers_list):
        # накопитель суммы
        total = 0
        for value in numbers_list:
            total += value
        return total

    # Показать сумму значений списка
    print(f'Сумма значений элементов списка: {get_total(numbers)}.')


if __name__ == '__main__':
    main()