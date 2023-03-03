import random
ROWS = 3    # Определить количество строк
COLS = 2    # Определить количество колонок
def main():
    # Создать "нулевой список"
    values = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]

    # Заполнить список случайными значениями
    for r in range(ROWS):
        for c in range(COLS):
            values[r][c] = random.randint(1, 100)

    print(values)


if __name__ == '__main__':
    main()
