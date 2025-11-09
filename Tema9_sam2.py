class Tomato: # Класс Tomato
    # Статическое свойство states - содержит все стадии созревания помидора
    states = {
        0: 'отсутствует',
        1: 'цветение',
        2: 'зеленый',
        3: 'красный'
    }

    def __init__(self, index):
        """
        Инициализация помидора
        _index - защищенное свойство (передается параметром)
        _state - защищенное свойство (принимает первое значение из словаря states)
        """
        self._index = index  # Защищенное свойство - индекс помидора
        self._state = 0  # Защищенное свойство - текущая стадия созревания

    def grow(self):
        """Метод для перевода томата на следующую стадию созревания"""
        if self._state < 3:  # Если томат еще не красный
            self._state += 1  # Переходим на следующую стадию
        print(f"Помидор {self._index} теперь {Tomato.states[self._state]}")

    def is_ripe(self):
        """Метод проверки, созрел ли томат"""
        return self._state == 3  # Возвращает True, если томат красный


class TomatoBush: # Класс TomatoBush
    def __init__(self, num_tomatoes):
        """
        Инициализация куста с помидорами
        tomatoes - динамическое свойство, содержащее список объектов Tomato
        """
        self.tomatoes = [Tomato(i) for i in range(num_tomatoes)]  # Создаем список томатов

    def grow_all(self):
        """Метод для перевода всех томатов на следующий этап созревания"""
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        """Метод проверки, все ли томаты созрели"""
        return all(tomato.is_ripe() for tomato in self.tomatoes)  # True если все томаты спелые

    def give_away_all(self):
        """Метод для очистки списка томатов после сбора урожая"""
        self.tomatoes = []  # Очищаем список томатов


class Gardener: # Класс Gardener
    def __init__(self, name, plant):
        """
        Инициализация садовника
        name - публичное свойство (имя садовника)
        _plant - защищенное свойство (объект класса TomatoBush)
        """
        self.name = name  # Публичное свойство - имя садовника
        self._plant = plant  # Защищенное свойство - растение для ухода

    @staticmethod
    def knowledge_base():
        """Статический метод для вывода справки по садоводству"""
        print("Справка по садоводству:")
        print("1. Помидор проходит 4 стадии созревания: отсутствует, цветение, зеленый, красный")
        print("2. Собирать урожай можно только когда все помидоры красные")
        print("3. Для роста помидоров нужно ухаживать за растением")
        print("4. После сбора урожая куст очищается")

    def work(self):
        """Метод для ухода за растением - заставляет растение расти"""
        print(f"{self.name} ухаживает за растением...")
        self._plant.grow_all()

    def harvest(self):
        """Метод для сбора урожая"""
        if self._plant.all_are_ripe():
            print(f"{self.name} собирает урожай! Все помидоры созрели.")
            self._plant.give_away_all()
            return True
        else:
            print(f"Предупреждение: {self.name}, еще не все помидоры созрели!")
            print("Продолжайте ухаживать за растением.")
            return False


bush = TomatoBush(3)
gardener = Gardener("Иван", bush)
print(f"Создан садовник: {gardener.name}")
print(f"Создан куст с {len(bush.tomatoes)} помидорами")