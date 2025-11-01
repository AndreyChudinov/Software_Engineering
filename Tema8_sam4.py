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