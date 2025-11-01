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