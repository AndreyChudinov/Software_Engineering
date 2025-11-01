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

# Создание нового класса ElectricCar, который наследуется от класса Car
class ElectricCar(Car):
    def __init__(self, make, model, battery_capacity):
        # Вызов конструктора родительского класса для инициализации общих атрибутов
        super().__init__(make, model)
        self.battery_capacity = battery_capacity  # Атрибут для хранения емкости батареи

    def charge(self):
        # Метод для имитации зарядки электрического автомобиля
        print(f"Charging the {self.make} {self.model} with {self.battery_capacity} kWh") # Вывод сообщения о зарядке


my_electric_car = ElectricCar("Tesla", "Model S", 75) # Создание объекта класса ElectricCar

my_electric_car.drive() # Вызов унаследованного метода drive для электрического автомобиля

my_electric_car.charge() # Вызов метода charge для зарядки электрического автомобиля