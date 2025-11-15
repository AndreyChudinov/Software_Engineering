def add_two():
    try:
        user_input = input("Введите число: ")
        number = float(user_input)
        result = 2 + number
        print(f"Результат: 2 + {number} = {result}")
        return result
    except ValueError:
        print("Неподходящий тип данных. Ожидалось число.")


if __name__ == "__main__":
    print("=== Тест 1: Ввод числа ===")
    add_two()

    print("\n=== Тест 2: Ввод строки ===")
    add_two()