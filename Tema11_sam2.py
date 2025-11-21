def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    with open('fib.txt', 'w', encoding='utf-8') as file:
        fib_generator = fib(200)
        result = None
        for num in fib_generator:
            file.write(f"{num}\n")
            result = num

    print(f"200-е число Фибоначчи: {result}")
    print("Все числа Фибоначчи записаны в файл 'fib.txt'")