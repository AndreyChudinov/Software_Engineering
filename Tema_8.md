## Тема 8. Основы объектно-ориентированного программирования

### Отчет по Теме #8 выполнил(а):
- Чудинов Андрей Игоревич  
- ИВТ-23-2
## Итоговая таблица выполнения заданий
| Задание      | Лаб_раб | Сам_раб |
|--------------|---------|---------|
| Задание 1    | +       | +       |
| Задание 2    | +       | +       |
| Задание 3    | +       | +       |
| Задание 4    | +       | +       |
| Задание 5    | +       | +       |

знак "+" — задание выполнено; знак "-" — задание не выполнено;
### Работу проверили:
- к.э.н., доцент Панов М.А.
## Лабораторная работа №1
*Создайте класс “Car” с атрибутами производитель и модель. Создайте объект этого класса. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями.*
```python
class Car: # Определяем класс "Car"
    def __init__(self, make, model):
        # Инициализация атрибутов класса
        self.make = make  # Атрибут для хранения производителя
        self.model = model  # Атрибут для хранения модели


my_car = Car("Toyota", "Corolla") # Создание объекта класса Car
print(f"Производитель: {my_car.make}, модель: {my_car.model}") # Выводим информацию о машине
```
## Результат.
<img width="745" height="525" alt="Image" src="https://github.com/user-attachments/assets/e7511600-9713-4a36-85b2-04ea50cf5009" />

## Выводы
*Создан базовый класс Car с атрибутами производитель и модель. Создан объект класса Car. Освоены основы создания класса и объекта.*

## Лабораторная работа №2
*Дополните код из первого задания, добавив в него атрибуты и методы класса, заставьте машину “поехать”. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.*
```python
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
```
## Результат.
<img width="753" height="525" alt="Image" src="https://github.com/user-attachments/assets/55b833e8-495f-40ed-b01e-f1e9a85449c3" />

## Выводы
*В класс Car добавлен метод drive, демонстрирующий поведение объекта. Изучено добавление методов в класс для описания действий.*

## Лабораторная работа №3
*Создайте новый класс “ElectricCar” с методом “charge” и атрибутом емкость батареи. Реализуйте его наследование от класса, созданного в первом задании. Заставьте машину поехать, а потом заряжаться. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.*
```python
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
```
## Результат.
<img width="755" height="520" alt="Image" src="https://github.com/user-attachments/assets/ba4b323a-4bdb-48a1-87e9-3fb10565a894" />

## Выводы
*Создан класс ElectricCar, унаследованный от Car, с добавлением нового атрибута емкость батареи и метода “charge”. Освоены принципы наследования.*

## Лабораторная работа №4
*Реализуйте инкапсуляцию для класса, созданного в первом задании. Создайте защищенный атрибут производителя и приватный атрибут модели. Вызовите защищенный атрибут и заставьте машину поехать. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.*
```python
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
```
## Результат.
<img width="753" height="519" alt="Image" src="https://github.com/user-attachments/assets/d35c0e6a-1303-4b4d-8b56-707e8d07ca75" />

## Выводы
*Реализована инкапсуляция в классе Car с использованием защищенного атрибута производителя и приватного атрибута модели. Изучены механизмы контроля доступа к данным класса.*

## Лабораторная работа №5
*Реализуйте полиморфизм создав основной (общий) класс “Shape”, а также еще два класса “Rectangle” и “Circle”. Внутри последних двух классов реализуйте методы для подсчета площади фигуры. После этого создайте массив с фигурами, поместите туда круг и прямоугольник, затем при помощи цикла выведите их площади. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.*
```python
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
```
## Результат.
<img width="752" height="514" alt="Image" src="https://github.com/user-attachments/assets/0bc9c4f0-f32e-430c-8024-b2d0d9aa69e1" />

## Выводы
*Освоено использование полиморфизма для единообразной работы с разными типами объектов.*

## Самостоятельная работа №1
*Самостоятельно создайте класс и его объект. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.*
```python
class Book:
    def __init__(self, title, author, year):
        # Инициализация атрибутов
        self.title = title    # Название книги
        self.author = author  # Автор книги
        self.year = year      # Год издания


# Создание объекта класса Book
my_book = Book("Война и мир", "Лев Толстой", 1869)
print(f"Книга: '{my_book.title}', автор: {my_book.author}, год: {my_book.year}")
```
## Результат.
<img width="759" height="423" alt="Image" src="https://github.com/user-attachments/assets/9e531c2e-73b2-4d97-9014-a5a24ecc012f" />

## Выводы
*Создан собственный класс Book и его объект my_book.*

## Самостоятельная работа №2
*Самостоятельно создайте атрибуты и методы для ранее созданного класса. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.*
```python
class Book:
    def __init__(self, title, author, year, genre, pages):
        # Инициализация атрибутов
        self.title = title      # Название книги
        self.author = author    # Автор книги
        self.year = year        # Год издания
        self.genre = genre      # Жанр книги
        self.pages = pages      # Количество страниц
        self.is_read = False    # Статус прочтения

    def read_book(self):
        """Метод для отметки о прочтении книги"""
        self.is_read = True
        print(f"Книга '{self.title}' прочитана!")

    def get_book_info(self):
        """Метод для получения полной информации о книге"""
        status = "прочитана" if self.is_read else "не прочитана"
        return f"'{self.title}' - {self.author} ({self.year}), {self.genre}, {self.pages} стр., {status}"

    def estimate_reading_time(self, reading_speed=50):
        """Метод для оценки времени чтения книги"""
        hours = self.pages / reading_speed
        return f"Примерное время чтения: {hours:.1f} часов"


# Создание объекта
my_book = Book("Война и мир", "Лев Толстой", 1869, "Роман", 1300)

# Демонстрация методов:
print(my_book.get_book_info())
print(my_book.estimate_reading_time())
my_book.read_book()
print(my_book.get_book_info())
```
## Результат.
<img width="974" height="413" alt="Image" src="https://github.com/user-attachments/assets/32b34d96-1881-4d10-a940-a058f29117b3" />

## Выводы
*Класс Book расширен новыми атрибутами и созданными методами.*

## Самостоятельная работа №3
*Самостоятельно реализуйте наследование, продолжая работать с ранее созданным классом. Оно должно отличаться, от того, что указано в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.*
```python
class Book:
    def __init__(self, title, author, year, genre, pages):
        # Инициализация атрибутов
        self.title = title      # Название книги
        self.author = author    # Автор книги
        self.year = year        # Год издания
        self.genre = genre      # Жанр книги
        self.pages = pages      # Количество страниц
        self.is_read = False    # Статус прочтения

    def read_book(self):
        """Метод для отметки о прочтении книги"""
        self.is_read = True
        print(f"Книга '{self.title}' прочитана!")

    def get_book_info(self):
        """Метод для получения полной информации о книге"""
        status = "прочитана" if self.is_read else "не прочитана"
        return f"'{self.title}' - {self.author} ({self.year}), {self.genre}, {self.pages} стр., {status}"

    def estimate_reading_time(self, reading_speed=50):
        """Метод для оценки времени чтения книги"""
        hours = self.pages / reading_speed
        return f"Примерное время чтения: {hours:.1f} часов"


class AudioBook(Book):
    """Класс аудиокниги, наследуется от Book"""
    def __init__(self, title, author, year, genre, duration, narrator):
        # Вызов конструктора родительского класса
        super().__init__(title, author, year, genre, 0)  # У аудиокниги нет страниц
        self.duration = duration    # Продолжительность в часах
        self.narrator = narrator    # Чтец аудиокниги
        self.format_type = "аудио"  # Тип формата

    def get_book_info(self):
        """Переопределение метода для аудиокниги"""
        status = "прослушана" if self.is_read else "не прослушана"
        return f"'{self.title}' - {self.author} ({self.year}), {self.genre}, {self.duration}ч., чтец: {self.narrator}, {status}"

    def estimate_reading_time(self):
        """Переопределение метода для аудиокниги"""
        return f"Продолжительность аудиокниги: {self.duration} часов"


# Создание объектов
my_book = Book("Война и мир", "Лев Толстой", 1869, "Роман", 1300)
audio_book = AudioBook("Мастер и Маргарита", "Михаил Булгаков", 1967, "Роман", 18, "Максим Суханов")

print("Обычная книга:")
print(my_book.get_book_info())
print("\nАудиокнига:")
print(audio_book.get_book_info())
print(audio_book.estimate_reading_time())
```
## Результат.
<img width="1048" height="361" alt="Image" src="https://github.com/user-attachments/assets/55d19f18-40db-49dd-b839-8fdfeafd13cd" />

## Выводы
*Реализовано наследование через создание класса AudioBook на основе Book.*

## Самостоятельная работа №4
*Самостоятельно реализуйте инкапсуляцию, продолжая работать с ранее созданным классом. Она должна отличаться, от того, что указана в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.*
```python
class Book:
    def __init__(self, title, author, year, genre, pages):
        # Изменяем атрибуты на защищенные и приватные
        self._title = title          # Защищенный атрибут названия
        self._author = author        # Защищенный атрибут автора
        self._genre = genre          # Защищенный атрибут жанра
        self.__year = year           # Приватный атрибут года издания
        self.__pages = pages         # Приватный атрибут количества страниц
        self.is_read = False         # Публичный атрибут статуса прочтения

    def read_book(self):
        """Метод для отметки о прочтении книги"""
        self.is_read = True
        print(f"Книга '{self._title}' прочитана!")

    def get_book_info(self):
        """Метод для получения полной информации о книге"""
        status = "прочитана" if self.is_read else "не прочитана"
        return f"'{self._title}' - {self._author} ({self.__year}), {self._genre}, {self.__pages} стр., {status}"

    def estimate_reading_time(self, reading_speed=50):
        """Метод для оценки времени чтения книги"""
        hours = self.__pages / reading_speed
        return f"Примерное время чтения: {hours:.1f} часов"


class AudioBook(Book):
    """Класс аудиокниги, наследуется от Book"""
    def __init__(self, title, author, year, genre, duration, narrator):
        # Вызов конструктора родительского класса
        super().__init__(title, author, year, genre, 0)  # У аудиокниги нет страниц
        self.duration = duration    # Продолжительность в часах
        self.narrator = narrator    # Чтец аудиокниги
        self.format_type = "аудио"  # Тип формата

    def get_book_info(self):
        """Переопределение метода для аудиокниги"""
        status = "прослушана" if self.is_read else "не прослушана"
        return f"'{self._title}' - {self._author} ({self._Book__year}), {self._genre}, {self.duration}ч., чтец: {self.narrator}, {status}"

    def estimate_reading_time(self):
        """Переопределение метода для аудиокниги"""
        return f"Продолжительность аудиокниги: {self.duration} часов"


# Создание объектов
my_book = Book("Война и мир", "Лев Толстой", 1869, "Роман", 1300)
audio_book = AudioBook("Мастер и Маргарита", "Михаил Булгаков", 1967, "Роман", 18, "Максим Суханов")

print("\nОбычная книга:")
print(my_book.get_book_info())
print(my_book.estimate_reading_time())

print("\nАудиокнига:")
print(audio_book.get_book_info())
print(audio_book.estimate_reading_time())

print("\nДемонстрация инкапсуляции:")
print(f"Доступ к защищенному атрибуту: {my_book._title}")
print(f"Доступ к защищенному атрибуту: {my_book._author}")

# Попытка доступа к приватным атрибутам
try:
    print(my_book.__year)  # Это вызовет ошибку
except AttributeError as e:
    print(f"Ошибка доступа к приватному атрибуту: {e}")
```
## Результат.
<img width="1030" height="593" alt="Image" src="https://github.com/user-attachments/assets/3db412f8-7beb-48a4-9867-1a6525305fad" />

## Выводы
*В классе Book атрибуты изменены на защищенные и приватные.*

## Самостоятельная работа №5
*Самостоятельно реализуйте полиморфизм. Он должен отличаться, от того, что указан в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.*
```python
class Book:
    def __init__(self, title, author, year, genre, pages):
        # Изменяем атрибуты на защищенные и приватные
        self._title = title          # Защищенный атрибут названия
        self._author = author        # Защищенный атрибут автора
        self._genre = genre          # Защищенный атрибут жанра
        self.__year = year           # Приватный атрибут года издания
        self.__pages = pages         # Приватный атрибут количества страниц
        self.is_read = False         # Публичный атрибут статуса прочтения

    def read_book(self):
        """Метод для отметки о прочтении книги"""
        self.is_read = True
        print(f"Книга '{self._title}' прочитана!")

    def get_book_info(self):
        """Метод для получения полной информации о книге"""
        status = "прочитана" if self.is_read else "не прочитана"
        return f"'{self._title}' - {self._author} ({self.__year}), {self._genre}, {self.__pages} стр., {status}"

    def estimate_reading_time(self, reading_speed=50):
        """Метод для оценки времени чтения книги"""
        hours = self.__pages / reading_speed
        return f"Примерное время чтения: {hours:.1f} часов"

    def get_format_type(self):
        """Метод для получения типа формата"""
        return "печатная книга"


class AudioBook(Book):
    """Класс аудиокниги, наследуется от Book"""
    def __init__(self, title, author, year, genre, duration, narrator):
        # Вызов конструктора родительского класса
        super().__init__(title, author, year, genre, 0)  # У аудиокниги нет страниц
        self.duration = duration    # Продолжительность в часах
        self.narrator = narrator    # Чтец аудиокниги
        self.format_type = "аудио"  # Тип формата

    def get_book_info(self):
        """Переопределение метода для аудиокниги"""
        status = "прослушана" if self.is_read else "не прослушана"
        return f"'{self._title}' - {self._author} ({self._Book__year}), {self._genre}, {self.duration}ч., чтец: {self.narrator}, {status}"

    def estimate_reading_time(self):
        """Переопределение метода для аудиокниги"""
        return f"Продолжительность аудиокниги: {self.duration} часов"

    def get_format_type(self):
        """Переопределение метода для аудиокниги"""
        return self.format_type


class EBook(Book):
    """Класс электронной книги, наследуется от Book"""
    def __init__(self, title, author, year, genre, pages, file_format):
        # Вызов конструктора родительского класса
        super().__init__(title, author, year, genre, pages)
        self.file_format = file_format  # Формат файла
        self.file_size = pages * 0.05   # Примерный размер файла в MB

    def get_book_info(self):
        """Переопределение метода для электронной книги"""
        status = "прочитана" if self.is_read else "не прочитана"
        return f"'{self._title}' - {self._author} ({self._Book__year}), {self._genre}, {self._Book__pages} стр., {self.file_format}, {status}"

    def estimate_reading_time(self, reading_speed=50):
        """Переопределение метода для электронной книги"""
        hours = self._Book__pages / reading_speed
        return f"Примерное время чтения: {hours:.1f} часов (электронный формат)"

    def get_format_type(self):
        """Переопределение метода для электронной книги"""
        return f"электронная книга ({self.file_format})"


# Создание объектов разных типов книг
books = [
    Book("Война и мир", "Лев Толстой", 1869, "Роман", 1300),
    AudioBook("Мастер и Маргарита", "Михаил Булгаков", 1967, "Роман", 18, "Максим Суханов"),
    EBook("1984", "Джордж Оруэлл", 1949, "Антиутопия", 346, "PDF"),
    Book("Преступление и наказание", "Федор Достоевский", 1866, "Роман", 672),
    AudioBook("Анна Каренина", "Лев Толстой", 1877, "Роман", 22, "Александр Клюквин")
]

# Демонстрация полиморфизма:
print("1. Информация о всех книгах:")
for book in books:
    print(f"- {book.get_book_info()}")

print("\n2. Форматы всех книг:")
for book in books:
    print(f"- {book.get_format_type()}")
```
## Результат.
<img width="974" height="453" alt="Image" src="https://github.com/user-attachments/assets/0156f6f2-0213-40cd-8566-4bea75661868" />

## Выводы
*Продемонстрировано использование полиморфизма для работы с разнотипными объектами в едином стиле.*

## Общие выводы по теме
*В ходе изучения темы были освоены следующие ключевые концепции ООП:
1) Классы и объекты:
- Класс — это шаблон или "чертеж", который определяет структуру и поведение объектов определенного типа. Класс описывает, какие данные (атрибуты) будут содержать объекты и какие операции (методы) они смогут выполнять.
- Объект (или экземпляр класса) — это конкретная реализация класса, созданная в памяти. Каждый объект имеет свое уникальное состояние (значения атрибутов) и может выполнять поведение, определенное в классе (методы).
2) Инкапсуляция
- Инкапсуляция — это принцип ООП, который заключается в объединении данных и методов, которые с ними работают, в единый объект и ограничении доступа к внутреннему состоянию объекта из внешней среды. Инкапсуляция позволяет скрыть детали реализации, защитить данные от неконтролируемого изменения, предоставить контролируемый интерфейс для работы с объектом.
3) Наследование
- Наследование — это механизм, который позволяет создать новый класс на основе существующего. Дочерний класс получает атрибуты и методы родительского класса, но может расширять и модифицировать эту функциональность.
4) Полиморфизм
- Полиморфизм — это способность объектов разных классов реагировать на одинаковые методы или операции по-разному.*



































