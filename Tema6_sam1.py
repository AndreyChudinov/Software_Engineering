user_input = input("Введите последовательность чисел: ")

numbers_list = [int(num) for num in user_input.split()]

numbers_tuple = tuple(numbers_list)

print("Список:", numbers_list)
print("Кортеж:", numbers_tuple)