## Тема 11. Итераторы и генераторы

### Отчет по Теме #11 выполнил(а):
- Чудинов Андрей Игоревич  
- ИВТ-23-2
## Итоговая таблица выполнения заданий
| Задание      | Лаб_раб | Сам_раб |
|--------------|---------|---------|
| Задание 1    | +       | +       |
| Задание 2    | +       | +       |
| Задание 3    | +       |         |
| Задание 4    | +       |         |
| Задание 5    | +       |         |

знак "+" — задание выполнено; знак "-" — задание не выполнено;
### Работу проверили:
- к.э.н., доцент Панов М.А.
## Лабораторная работа №1
*Простой итератор, но у него нет гибкой настройки, например его нельзя развернуть. Он работает просто как next(), но нет prev()*
```python
numbers = [0, 1, 2, 3, 4, 5]
for item in numbers:
    print(item)
```
## Результат.
<img width="475" height="456" alt="Image" src="https://github.com/user-attachments/assets/4b9e626d-3028-4066-9b69-3575c47b23b3" />

## Выводы
*Демонстрация базового итератора без возможности настройки*

## Лабораторная работа №2
*Класс итератор с гибкой настройкой и удобными применением*
```python
class CountDown:
    def __init__(self, start):
        self.count = start + 1

    def __iter__(self):
        return self

    def __next__(self):
        self.count -= 1
        if self.count < 0:
            raise StopIteration
        return self.count


if __name__ == '__main__':
    counter = CountDown(5)
    for i in counter:
        print(i)
```
## Результат.
<img width="478" height="446" alt="Image" src="https://github.com/user-attachments/assets/85647f70-7ed4-4932-a76d-db41e9826be6" />

## Выводы
*Создание собственного класса итератора с возможностью гибкого управления процессом.*

## Лабораторная работа №3
*Генератор списка*
```python
a = [i ** 2 for i in range(1, 5)]

print('a - ', a)
for i in a:
    print(i)

print('iter(a) - ', iter(a))
for i in a:
    print(i)
```
## Результат.
<img width="663" height="504" alt="Image" src="https://github.com/user-attachments/assets/8dba2978-691e-44e9-a548-d6a374db360a" />

## Выводы
*Генерация списка квадратов чисел через конструкцию выражения-списка.*

## Лабораторная работа №4
*Выражения генераторы*
```python
b = (i ** 2 for i in range(1, 5))
print(b) # вывод не такой, как у генератора списков
print('first')
for i in b:
    print(i)
print('second')
# из-за особенностей выражений генераторов,
# они не будут выводиться больше одного раза
for i in b:
    print(i)
```
## Результат.
<img width="661" height="507" alt="Image" src="https://github.com/user-attachments/assets/3cc2186f-2642-4a7a-9c78-9854ec543c58" />

## Выводы
*Генераторное выражение для вычисления квадратов чисел. Первый цикл for выдает значения 1, 4, 9, 16, а второй – не выдаёт ничего, так как все значения уже были сгенерированы.*

## Лабораторная работа №5
*Такой же счетчик, как и в первом задании, только это генератор и использует yield*
```python
def countdown(count):
    while count >= 0:
        yield count
        count -= 1


if __name__ == '__main__':
    counter = countdown(5)
    for i in counter:
        print(i)
```
## Результат.
<img width="375" height="535" alt="Image" src="https://github.com/user-attachments/assets/4d258c69-711b-40a8-a6c1-b35fa958dc3b" />

## Выводы
*Реализация функции-генератора с использованием yield.*

## Самостоятельная работа №1
**
```python

```
## Результат.


## Выводы
**

## Самостоятельная работа №2
**
```python

```
## Результат.


## Выводы
**


















