class Car: # Определяем класс "Car"
    def __init__(self, make, model):
        # Инициализация атрибутов класса
        self._make = make # Защищенный атрибут для хранения производителя
        self.__model = model # Приватный атрибут для хранения модели

    def drive(self):
        # Метод для имитации движения автомобиля
        print(f"Driving the {self._make} {self.__model}") # Вывод сообщения о движении автомобиля


my_car = Car("Toyota", "Corolla") # Создание объекта класса Car
print(my_car._make) # Доступ к защищенному атрибуту
# print(my_car.__model) # Ошибка! Приватный атрибут не доступен
my_car.drive() # Вызов метода drive для объекта my_car