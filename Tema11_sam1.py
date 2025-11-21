def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    fib_generator = fib(200)
    result = None
    for num in fib_generator:
        result = num
    print(f"200-е число Фибоначчи: {result}")