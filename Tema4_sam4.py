def calculate_average(*args):
    if len(args) == 0:
        return 0

    total = sum(args)
    average = total / len(args)
    return average


if __name__ == '__main__':
    # Вычисляем и выводим среднее арифметическое для различных наборов чисел

    # Пример с тремя числами
    result1 = calculate_average(1, 2, 3)
    print(f"Среднее арифметическое для чисел 1, 2, 3: {result1}")

    # Пример с четырьмя числами
    result2 = calculate_average(10, 20, 30, 40)
    print(f"Среднее арифметическое для чисел 10, 20, 30, 40: {result2}")

    # Пример с одним числом
    result3 = calculate_average(42)
    print(f"Среднее арифметическое для числа 42: {result3}")

    # Пример без аргументов
    result4 = calculate_average()
    print(f"Среднее арифметическое без аргументов: {result4}")