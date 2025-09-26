num = input('Введите число от 0 до 10: ')
if not num.isdigit() or not (0 <= int(num) <= 10):
    print('Число не подходит по требованиям!')
    exit()
num = int(num)
if 0 <= num <= 3:
    print('Диапазон: от 0 до 3 включительно')
elif num < 6:
    print('Диапазон: от 3 до 6')
else: print('Диапазон: от 6 до 10 включительно')