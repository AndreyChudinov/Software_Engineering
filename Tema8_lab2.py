class Car: # Определяем класс "Car"
    def __init__(self, make, model):
        # Инициализация атрибутов класса
        self.make = make  # Атрибут для хранения производителя
        self.model = model  # Атрибут для хранения модели

    def drive(self):
        # Метод для имитации движения автомобиля
        print(f"Driving the {self.make} {self.model}") # Вывод сообщения о движении автомобиля


my_car = Car("Toyota", "Corolla") # Создание объекта класса Car

my_car.drive() # Вызов метода drive для объекта my_car