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




























































