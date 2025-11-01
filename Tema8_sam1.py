class Book:
    def __init__(self, title, author, year):
        # Инициализация атрибутов
        self.title = title    # Название книги
        self.author = author  # Автор книги
        self.year = year      # Год издания


# Создание объекта класса Book
my_book = Book("Война и мир", "Лев Толстой", 1869)
print(f"Книга: '{my_book.title}', автор: {my_book.author}, год: {my_book.year}")