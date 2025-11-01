class Shape:
    """Базовый класс для всех фигур"""
    def area(self):
        # Метод area будет переопределен в дочерних классах
        pass


class Rectangle(Shape):
    """Класс прямоугольника, наследуется от Shape"""
    def __init__(self, width, height):
        # Инициализация атрибутов прямоугольника
        self.width = width   # Ширина прямоугольника
        self.height = height # Высота прямоугольника

    def area(self):
        # Реализация метода area для прямоугольника
        return self.width * self.height


class Circle(Shape):
    """Класс круга, наследуется от Shape"""
    def __init__(self, radius):
        # Инициализация атрибута круга
        self.radius = radius  # Радиус круга

    def area(self):
        # Реализация метода area для круга
        return 3.14 * self.radius * self.radius


# Создание объектов
rectangle = Rectangle(5, 4)  # Прямоугольник шириной 5 и высотой 4
circle = Circle(3)           # Круг с радиусом 3

shapes = [rectangle, circle] # Создание массива фигур

# Вывод площадей фигур с помощью цикла
for shape in shapes:  # Проходим по всем фигурам в массиве
    print(shape.area())  # Выводим площадь текущей фигуры