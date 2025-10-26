import csv
import os
from datetime import datetime

EXPENSES_FILE = "Tema7_sam2_expenses.csv"


def initialize_file():
    """Создает файл для хранения расходов, если он не существует"""
    if not os.path.exists(EXPENSES_FILE):
        with open(EXPENSES_FILE, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Дата", "Сумма", "Категория", "Описание"])
        print(f"Создан новый файл для учета расходов: {EXPENSES_FILE}")


def add_expense():
    """Добавляет новый расход в файл"""
    print("\n=== Добавление нового расхода ===")

    while True:
        date_input = input("Введите дату (ГГГГ-ММ-ДД) или нажмите Enter для использования сегодняшней даты: ")
        if not date_input:
            expense_date = datetime.now().strftime("%Y-%m-%d")
            break
        try:
            datetime.strptime(date_input, "%Y-%m-%d")
            expense_date = date_input
            break
        except ValueError:
            print("Некорректный формат даты. Пожалуйста, используйте формат ГГГГ-ММ-ДД.")

    while True:
        amount_input = input("Введите сумму расхода: ")
        try:
            amount = float(amount_input)
            if amount <= 0:
                print("Сумма должна быть положительным числом.")
                continue
            break
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число.")

    category = input("Введите категорию расхода (продукты, транспорт, развлечения и т.д.): ").strip()
    if not category:
        category = "Прочее"

    description = input("Введите описание расхода (необязательно): ").strip()

    with open(EXPENSES_FILE, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([expense_date, amount, category, description])

    print("\nРасход успешно добавлен!")


def display_expenses(expenses):
    """Отображает список расходов в удобном формате"""
    if not expenses:
        print("\nНет расходов, соответствующих критериям.")
        return

    print("\n{:<12} {:<10} {:<15} {}".format("Дата", "Сумма", "Категория", "Описание"))
    print("-" * 70)

    total = 0
    for expense in expenses:
        date, amount, category, description = expense
        total += float(amount)
        print("{:<12} {:<10.2f} {:<15} {}".format(date, float(amount), category, description))

    print("-" * 70)
    print("{:<12} {:<10.2f}".format("Итого:", total))


def view_all_expenses():
    """Показывает все расходы из файла"""
    print("\n=== Все расходы ===")

    try:
        with open(EXPENSES_FILE, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            expenses = list(reader)

        display_expenses(expenses)
    except FileNotFoundError:
        print("Файл с расходами не найден. Добавьте первый расход.")


def view_expenses_by_date():
    """Показывает расходы за определенный период"""
    print("\n=== Просмотр расходов по дате ===")

    try:
        with open(EXPENSES_FILE, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            all_expenses = list(reader)

        if not all_expenses:
            print("Нет записанных расходов.")
            return

        print("\nДоступные даты:")
        unique_dates = sorted(set(expense[0] for expense in all_expenses))
        for i, date in enumerate(unique_dates, 1):
            print(f"{i}. {date}")

        while True:
            choice = input("\nВведите номер даты или нажмите Enter для возврата: ")
            if not choice:
                return

            try:
                index = int(choice) - 1
                if 0 <= index < len(unique_dates):
                    selected_date = unique_dates[index]
                    filtered_expenses = [exp for exp in all_expenses if exp[0] == selected_date]
                    print(f"\nРасходы за {selected_date}:")
                    display_expenses(filtered_expenses)
                    break
                else:
                    print("Некорректный номер.")
            except ValueError:
                print("Пожалуйста, введите число.")

    except FileNotFoundError:
        print("Файл с расходами не найден. Добавьте первый расход.")


def view_expenses_by_category():
    """Показывает расходы по категории"""
    print("\n=== Просмотр расходов по категории ===")

    try:
        with open(EXPENSES_FILE, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            all_expenses = list(reader)

        if not all_expenses:
            print("Нет записанных расходов.")
            return

        print("\nДоступные категории:")
        unique_categories = sorted(set(expense[2] for expense in all_expenses))
        for i, category in enumerate(unique_categories, 1):
            print(f"{i}. {category}")

        while True:
            choice = input("\nВведите номер категории или нажмите Enter для возврата: ")
            if not choice:
                return

            try:
                index = int(choice) - 1
                if 0 <= index < len(unique_categories):
                    selected_category = unique_categories[index]
                    filtered_expenses = [exp for exp in all_expenses if exp[2] == selected_category]
                    print(f"\nРасходы в категории '{selected_category}':")
                    display_expenses(filtered_expenses)
                    break
                else:
                    print("Некорректный номер.")
            except ValueError:
                print("Пожалуйста, введите число.")

    except FileNotFoundError:
        print("Файл с расходами не найден. Добавьте первый расход.")


def main():
    """Основная функция программы"""
    initialize_file()

    while True:
        print("\n" + "=" * 50)
        print("Меню учета расходов")
        print("=" * 50)
        print("1. Добавить новый расход")
        print("2. Просмотреть все расходы")
        print("3. Просмотреть расходы по дате")
        print("4. Просмотреть расходы по категории")
        print("5. Выход")
        print("=" * 50)

        choice = input("Выберите действие (1-5): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_all_expenses()
        elif choice == '3':
            view_expenses_by_date()
        elif choice == '4':
            view_expenses_by_category()
        elif choice == '5':
            print("\nСпасибо за использование программы учета расходов!")
            break
        else:
            print("Некорректный выбор. Пожалуйста, введите число от 1 до 5.")


if __name__ == "__main__":
    main()