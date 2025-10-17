def analyze_grades():
    input_str = input("Введите оценки через запятую (например, 2, 3, 4, 5): ")

    try:
        grades = [int(grade.strip()) for grade in input_str.split(',')]
        grades_tuple = tuple(grades)
    except ValueError:
        print("Ошибка: введите корректные числа")
        return None, None

    fives_count = grades_tuple.count(5)
    has_twos = 2 in grades_tuple

    return fives_count, has_twos


if __name__ == "__main__":
    fives_count, has_twos = analyze_grades()

    if fives_count is not None:
        print("\nРезультаты анализа:")
        print(f"Количество пятерок: {fives_count}")
        print(f"Есть ли двойки: {'Да' if has_twos else 'Нет'}")