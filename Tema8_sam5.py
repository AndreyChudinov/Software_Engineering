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