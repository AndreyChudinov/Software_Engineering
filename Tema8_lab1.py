class Car: # Определяем класс "Car"
    def __init__(self, make, model):
        # Инициализация атрибутов класса
        self.make = make  # Атрибут для хранения производителя
        self.model = model  # Атрибут для хранения модели


my_car = Car("Toyota", "Corolla") # Создание объекта класса Car
print(f"Производитель: {my_car.make}, модель: {my_car.model}") # Выводим информацию о машине