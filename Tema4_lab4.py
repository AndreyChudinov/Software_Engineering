def main(x, *args):
    one = x # 10
    two = sum(args) # 0, 1, 2, -1, 0, -1, 1, 2
    three = float(len(args)) # длина кортежа args
    # пример работы операций над параметрами функции
    print(f"one={one}\ntwo={two}\nthree={three}")

    return x + sum(args) / float(len(args))


if __name__ == '__main__':
    result = main(10, 0, 1, 2, -1, 0, -1, 1, 2)
    print(f"\nresult={result}")