import time
from multiprocessing import Process, Queue
from functools import lru_cache

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

@lru_cache(maxsize=None)
def fibonacci_cached(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)

def compute_fibonacci(n, queue):
    result = fibonacci(n)
    queue.put(result)

if __name__ == '__main__':
    n = 100

    # Версия без декоратора
    start_time = time.time()
    queue = Queue()
    p = Process(target=compute_fibonacci, args=(n, queue))
    p.start()
    p.join(timeout=10)

    if p.is_alive():
        p.terminate()
        p.join()
        print("Вычисление F(100) без декоратора: не завершено за 10 секунд")
        print("Время выполнения без декоратора: >10 секунд")
    else:
        result = queue.get()
        elapsed = time.time() - start_time
        print(f"Вычисление F(100) без декоратора: {result}")
        print(f"Время выполнения без декоратора: {elapsed:.1f} секунд")

    # Версия с декоратором
    start_time = time.time()
    result_cached = fibonacci_cached(n)
    elapsed_cached = time.time() - start_time
    print(f"Вычисление F(100) с декоратором: {result_cached}")
    print(f"Время выполнения с декоратором: {elapsed_cached:.1f} секунд")