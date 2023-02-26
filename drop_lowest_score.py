def main():
    # Получить от пользователя оценки
    scores = get_scores()
    # Получить сумму оценок
    total = get_total(scores)
    # Получить минимальную оценку
    lowest = min(scores)
    # Вычесть самую низкую оценку из суммы
    total -= lowest
    # Вычислить среднее значение, с учетом отброшенной минимальной оценки
    average = total /(len(scores) - 1)

    # Показать среднее значение
    print(f'Средняя оценка с учетом отброшенной самой низкой оценки: {average}')


    # Функция get_scores получает от пользователя
    # серию оценок и сохраняет их в списке.
    # Указанная функция возвращает ссылку на список.
def get_scores():
    # Создается пустой список
    test_scores = []
    # Создается переменная для управления списком
    again = 'y'
    # Получить оценку и добавить её в список
    while again == 'y':
        value = float(input('Введите оценку: '))
        test_scores.append(value)

        # Продолжать или нет?
        print('Добавить ещё одну оценку?')
        again = input('y/n: ')
        print()
    return test_scores

    # get_total принимает список в качестве аргумента
    # и возвращает сумму значений
def get_total(value_list):
    # Накопитель
    total = 0.0
    for value in value_list:
        total += value
    return total


if __name__ == '__main__':
    main()
