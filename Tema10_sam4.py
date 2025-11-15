class CallLogger:
    """
    Декоратор класса для логирования вызовов функций.
    Отслеживает количество вызовов и выводит информацию о каждом вызове.
    """

    def __init__(self, func):
        # Сохраняем исходную функцию, которую будем декорировать
        self.func = func
        # Счетчик для отслеживания количества вызовов функции
        self.call_count = 0

    def __call__(self, *args, **kwargs):
        """
        Метод, который вызывается при каждом вызове декорированной функции.
        *args - позиционные аргументы
        **kwargs - именованные аргументы
        """
        # Увеличиваем счетчик вызовов при каждом вызове функции
        self.call_count += 1

        # Вызываем исходную функцию с переданными аргументами
        result = self.func(*args, **kwargs)

        # Выводим информацию о вызове: номер вызова, имя функции и результат
        print(f"Вызов {self.call_count}: {self.func.__name__} -> {result}")

        # Возвращаем результат исходной функции
        return result


@CallLogger
def calculate_area(length, width):
    """
    Вычисляет площадь прямоугольника.

    Args:
        length (int/float): Длина прямоугольника
        width (int/float): Ширина прямоугольника

    Returns:
        int/float: Площадь прямоугольника (length * width)
    """
    return length * width


@CallLogger
def greet_user(name, age, city=None):
    """
    Создает персонализированное приветствие.

    Args:
        name (str): Имя пользователя
        age (int): Возраст пользователя
        city (str, optional): Город пользователя

    Returns:
        str: Приветственное сообщение с информацией о пользователе
    """
    greeting = f"Привет, {name}! ({age} лет)"
    if city:
        greeting += f" из {city}"
    return greeting


if __name__ == "__main__":
    """
    Основной блок программы для демонстрации работы декоратора.
    Вызываем декорированные функции, чтобы показать работу CallLogger.
    """

    # Вызываем функцию calculate_area с разными параметрами
    calculate_area(5, 3)  # Должно вывести: Вызов 1: calculate_area -> 15
    calculate_area(10, 7)  # Должно вывести: Вызов 2: calculate_area -> 70

    # Вызываем функцию greet_user с разными параметрами
    greet_user("Анна", 25)  # Без указания города
    greet_user("Иван", 30, "Москва")  # С указанием города