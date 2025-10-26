## Тема 7. Работа с файлами (ввод, вывод)

### Отчет по Теме #7 выполнил(а):
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
| Задание 6    | +       |         |
| Задание 7    | +       |         |
| Задание 8    | +       |         |
| Задание 9    | +       |         |
| Задание 10   | +       |         |

знак "+" — задание выполнено; знак "-" — задание не выполнено;
### Работу проверили:
- к.э.н., доцент Панов М.А.
## Лабораторная работа №1
*Составьте текстовый файл и положите его в одну директорию с программой на Python. Текстовый файл должен состоять минимум из двух строк.*
```python
Hello students!
Lets talk about work with files on Python
```
## Результат.
<img width="974" height="468" alt="Image" src="https://github.com/user-attachments/assets/ddbba390-89f1-4df5-bb24-329d2f2d406b" />

## Выводы
*Создан текстовый файл с двумя строками для последующих экспериментов.*

## Лабораторная работа №2
*Напишите программу, которая выведет только первую строку из вашего файла, при этом используйте конструкцию open()/close().*
```python
f = open('Tema7_lab1_input.txt', 'r')
print(f.readline())
f.close()
```
## Результат.
<img width="798" height="412" alt="Image" src="https://github.com/user-attachments/assets/9bc1cd14-c8ec-42d3-8715-af6ff5bcc82d" />

## Выводы
*Программа выводит первую строку файла с использованием open()/close().*

## Лабораторная работа №3
*Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию open()/close().*
```python
f = open('Tema7_lab1_input.txt', 'r')
print(f.readlines())
f.close()
```
## Результат.
<img width="974" height="412" alt="Image" src="https://github.com/user-attachments/assets/d67b6dda-1a7e-48c6-bc8b-337fde104938" />

## Выводы
*Программа выводит все строки файла в массиве, используя open()/close().*

## Лабораторная работа №4
*Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию with open().*
```python
with open('Tema7_lab1_input.txt') as f:
    print(f.readlines())
```
## Результат.
<img width="841" height="359" alt="Image" src="https://github.com/user-attachments/assets/374b3f64-23d7-4c59-9579-1a358a001272" />

## Выводы
*Программа выводит все строки файла в массиве, используя with open().*

## Лабораторная работа №5
*Напишите программу, которая выведет каждую строку из вашего файла отдельно, при этом используйте конструкцию with open().*
```python
with open('Tema7_lab1_input.txt') as f:
    for line in f:
        print(line)
```
## Результат.
<img width="974" height="411" alt="Image" src="https://github.com/user-attachments/assets/abff21e8-c9ca-4a71-93da-5ccdec2eac47" />

## Выводы
*Программа построчно выводит содержимое файла с использованием with open().*

## Лабораторная работа №6
*Напишите программу, которая будет добавлять новую строку в ваш файл, а потом выведет полученный файл в консоль. Вывод можно осуществлять любым способом. Обязательно проверьте сам файл, чтобы изменения в нем тоже отображались.*
```python
with open('Tema7_lab1_input.txt', 'a+') as f:
    f.write('\nIm additional line')

with open('Tema7_lab1_input.txt', 'r') as f:
    result = f.readlines()
    print(result)
```
## Результат.
<img width="922" height="318" alt="Image" src="https://github.com/user-attachments/assets/2ff75dbf-8aad-4380-9e09-337ea8423791" />

<img width="638" height="448" alt="Image" src="https://github.com/user-attachments/assets/29811957-72c5-46bb-8547-c484a7aa8fc2" />

## Выводы
*Программа добавляет новую строку в файл и выводит обновлённое содержимое.*

## Лабораторная работа №7
*Напишите программу, которая перепишет всю информацию, которая была у вас в файле до этого, например напишет любые данные из произвольно вами составленного списка. Также не забудьте проверить что измененная вами информация сохранилась в файле.*
```python
lines = ['one', 'two', 'three']
with open('Tema7_lab1_input.txt', 'w') as f:
    for line in lines:
        f.write('\nCycle run ' + line)
    print('Done!')
```
## Результат.
<img width="546" height="377" alt="Image" src="https://github.com/user-attachments/assets/b0de4130-d76c-40a7-98f1-42b842ce964a" />

<img width="678" height="477" alt="Image" src="https://github.com/user-attachments/assets/3ba7ab78-e50b-475b-9a4a-d98430c158be" />

<img width="560" height="467" alt="Image" src="https://github.com/user-attachments/assets/36ab7f1c-dd32-4c64-878d-942c7f0cf3bc" />

## Выводы
*Программа перезаписывает файл данными из списка.*

## Лабораторная работа №8
*Выберите любую папку на своем компьютере, имеющую вложенные директории. Выведите на печать в терминал её содержимое, как и всех подкаталогов при помощи функции print_docs(directory).*
```python
import os


def print_docs(directory):
    all_files = os.walk(directory)
    for catalog in all_files:
        print(f'Папка {catalog[0]} содержит:')
    print(f'Директории: {", ".join([folder for folder in catalog[1]])}')
    print(f'Файлы: {", ".join([file for file in catalog[2]])}')
    print('-' * 40)


print_docs('C:/Users/ЛилияАндрей/Desktop/Учебники')
```
## Результат.
<img width="1056" height="510" alt="Image" src="https://github.com/user-attachments/assets/2604f020-51d3-4dec-afaa-bfcf0fb0277c" />

## Выводы
*Программа выводит содержимое выбранной папки и её подкаталогов.*

## Лабораторная работа №9
*Документ «input.txt» содержит следующий текст:

Приветствие

Спасибо

Извините

Пожалуйста

До свидания

Ты готов?

Как дела?

С днем рождения!

Удача!

Я тебя люблю.

Требуется реализовать функцию, которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько). Проверьте работоспособность программы на своем наборе данных*
```python
def longest_words(file):
    with open(file, encoding='utf-8') as f:
        words = f.read().split()
        max_length = len(max(words, key=len))
        sought_words = []
        for word in words:
            if len(word) == max_length:
                sought_words.append(word)

        if len(sought_words) == 1:
            return sought_words[0]
        return sought_words

print(longest_words('Tema7_lab9_input.txt'))
```
## Результат.
<img width="590" height="430" alt="Image" src="https://github.com/user-attachments/assets/fb96abd3-afc2-4d75-b4cc-af74e6204f5c" />

## Выводы
*Программа выводит слово (или список слов) максимальной длины в файле.*

## Лабораторная работа №10
*Требуется создать csv-файл «rows_300.csv» со следующими столбцами:
- № - номер по порядку (от 1 до 300);
- Секунда – текущая секунда на вашем ПК;
- Микросекунда – текущая миллисекунда на часах.

Для наглядности на каждой итерации цикла искусственно приостанавливайте скрипт на 0,01 секунды.*
```python
import csv
import datetime
import time

with open('rows_300.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['№', 'Секунда ', 'Микросекунда'])
    for line in range(1, 301):
        writer.writerow([line, datetime.datetime.now().second, datetime.datetime.now().microsecond])
        time.sleep(0.01)
```
## Результат.
<img width="974" height="470" alt="Image" src="https://github.com/user-attachments/assets/04f85b31-5b7f-4c57-8c7f-52ba1d7d344e" />

<img width="974" height="873" alt="Image" src="https://github.com/user-attachments/assets/08e0d606-40e9-402f-bd56-290fe6a48efe" />

## Выводы
*Программа создает CSV-файл «rows_300.csv» с указанными данными.*

## Самостоятельная работа №1
*Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте её содержимое в файл и напишите программу, которая считает количество слов в текстовом файле и определит самое часто встречающееся слово. Результатом выполнения задачи будет: скриншот файла со статьей, листинг кода, и вывод в консоль, в котором будет указана вся необходимая информация.*
```python
import string
from collections import Counter


def analyze_text(file_path):
    try:
        # Читаем содержимое файла
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read().lower()

        # Удаляем знаки препинания
        text = text.translate(str.maketrans('', '', string.punctuation))

        # Разделяем на слова и считаем их количество
        words = text.split()
        total_words = len(words)

        # Если файл пустой
        if total_words == 0:
            print("Файл пустой или не содержит слов.")
            return

        # Подсчитываем частоту слов
        word_counts = Counter(words)
        most_common_word, frequency = word_counts.most_common(1)[0]

        # Выводим результаты
        print(f"Общее количество слов в файле: {total_words}")
        print(f"Самое часто встречающееся слово: '{most_common_word}' (встречается {frequency} раз)")

    except FileNotFoundError:
        print(f"Ошибка: файл '{file_path}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    analyze_text("C:/Users/ЛилияАндрей/Desktop/Test.txt")
```
## Результат.
<img width="974" height="424" alt="Image" src="https://github.com/user-attachments/assets/d92db3f9-189e-4319-bd7b-fca1c3627a33" />

<img width="1045" height="630" alt="Image" src="https://github.com/user-attachments/assets/4eb82910-a431-44fe-b2e0-f9d463ca5573" />

## Выводы
*Программа анализирует текст в файле: подсчёт слов, поиск самого частого слова.*

## Самостоятельная работа №2
*У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не устраивает и нужно все делать самому. Напишите программу для учета расходов. Программа должна позволять вводить информацию о расходах, сохранять ее в файл и выводить существующие данные в консоль. Ввод информации происходит через консоль. Результатом выполнения задачи будет: скриншот файла с учетом расходов, листинг кода, и вывод в консоль, с демонстрацией работоспособности программы.*
```python
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
```
## Результат.
<img width="1048" height="491" alt="Image" src="https://github.com/user-attachments/assets/e98e00ad-1045-4e1e-a262-c5f1ca92116f" />

<img width="1049" height="459" alt="Image" src="https://github.com/user-attachments/assets/2e106769-2796-4e01-9182-162d1fac33ea" />

<img width="1043" height="513" alt="Image" src="https://github.com/user-attachments/assets/7bcb2146-7a11-4d7e-8449-f8e0372982fa" />

<img width="1043" height="501" alt="Image" src="https://github.com/user-attachments/assets/271bea71-6c5d-4ff0-9e18-b0136d11e9f4" />

<img width="770" height="609" alt="Image" src="https://github.com/user-attachments/assets/3632f9b3-8f09-4af8-a8c6-097d7a82c6db" />

<img width="697" height="319" alt="Image" src="https://github.com/user-attachments/assets/f056c087-8cff-4711-9658-447ac66fcc76" />

<img width="1044" height="304" alt="Image" src="https://github.com/user-attachments/assets/9ef8df5b-1bbb-427c-9e99-39eeff0d3aef" />

## Выводы
*Реализована программа для учёта расходов с сохранением в CSV-файл.*

## Самостоятельная работа №3
*Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк.

- Текст в файле:

Beautiful is better than ugly.

Explicit is better than implicit.

Simple is better than complex.

Complex is better than complicated.

- Ожидаемый результат:

Input file contains:

108 letters

20 words

4 lines*
```python
def analyze_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    lines = len(text.splitlines())

    words = len(text.split())

    letters = 0
    for char in text:
        if 'a' <= char.lower() <= 'z':
            letters += 1

    return letters, words, lines


letters, words, lines = analyze_text("Tema7_sam3_input.txt")

print("Input file contains:")
print(f"{letters} letters")
print(f"{words} words")
print(f"{lines} lines")
```
## Результат.
<img width="666" height="506" alt="Image" src="https://github.com/user-attachments/assets/d15b11ba-d46f-4293-9dd7-86bcba38a67d" />

<img width="674" height="545" alt="Image" src="https://github.com/user-attachments/assets/a578532f-f6c6-47c7-9e3a-b6466b796a85" />

## Выводы
*Программа анализирует текст в файле: подсчёт букв, слов и строк.*

## Самостоятельная работа №4
*Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звездочками \* (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра: если файл input.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и exAm должны быть заменены на \*\*\*\*.

- Запрещенные слова:

hello email python the exam wor is

- Предложение для проверки:

Hello, world! Python IS the programming language of thE future. My 

EMAIL is…. 

PYTHON is awesome!!!!
- Ожидаемый результат:

*****, ***ld! ****** ** *** programming language of *** future. My 

***** **….

****** ** awesome!!!!*
```python
import re


def censor_text():
    try:
        with open('Tema7_sam4_input.txt', 'r', encoding='utf-8') as file:
            banned_words = file.read().split()
    except FileNotFoundError:
        print("Ошибка: файл Tema7_sam4_input.txt не найден")
        return

    banned_words.sort(key=len, reverse=True)

    sentence = input("Введите предложение: ")

    for word in banned_words:
        pattern = re.compile(re.escape(word), re.IGNORECASE)
        sentence = pattern.sub('*' * len(word), sentence)

    print("\nРезультат:")
    print(sentence)


if __name__ == "__main__":
    censor_text()
```
## Результат.
<img width="1042" height="395" alt="Image" src="https://github.com/user-attachments/assets/94fae9cc-43a5-449e-8522-b1adae3aed56" />

<img width="670" height="570" alt="Image" src="https://github.com/user-attachments/assets/8d038264-6881-494f-a41d-29ca7fb9defa" />

## Выводы
*Программа заменяет запрещённые слова в тексте на звёздочки.*

## Самостоятельная работа №5
*Самостоятельно придумайте и решите задачу, которая будет взаимодействовать с текстовым файлом.

Задача: Программа должна запрашивать у пользователя его имя, создавать текстовый файл и записывать в него персональное приветствие.*
```python
name = input("Введите ваше имя: ")
with open("Tema7_sam5_hello.txt", "w", encoding="utf-8") as file:
    file.write(f"Привет, {name}! Рады видеть вас.")
print("Приветствие сохранено в файл Tema7_sam5_hello.txt")
```
## Результат.
<img width="714" height="333" alt="Image" src="https://github.com/user-attachments/assets/046fac24-0405-49eb-bf9d-9831c18bc88b" />

<img width="624" height="669" alt="Image" src="https://github.com/user-attachments/assets/33799911-06da-429c-853d-86e7d1097016" />

## Выводы
*Программа создает файл с персональным приветствием пользователя.*

## Общие выводы по теме
*В ходе выполнения лабораторных и самостоятельных работ были освоены ключевые аспекты работы с файлами в Python:

- Чтение данных: использование конструкций open()/close() и with open(), методы read(), readline(), readlines(), итерация по строкам.
- Запись данных: режимы записи ('w', 'a'), добавление и перезапись содержимого.
- Обработка текста: подсчёт слов, строк, поиск частых и самых длинных слов.
- Работа со структурированными данными: создание и запись CSV-файлов, организация данных в табличном формате.*
















































