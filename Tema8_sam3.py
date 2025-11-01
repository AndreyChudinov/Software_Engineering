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