import random
from collections import Counter


def find_top_numbers(sequence):
    counts = Counter(int(char) for char in sequence)

    top_3 = counts.most_common(3)

    top_3_sorted = sorted(top_3, key=lambda x: x[0])

    return dict(top_3_sorted)


if __name__ == "__main__":
    length = random.randint(15, 30)
    sequence = ''.join(str(random.randint(0, 9)) for _ in range(length))

    print(f"Случайная последовательность чисел ({length} символов):")
    print(sequence)

    result = find_top_numbers(sequence)
    print("\nТри самых часто встречающихся числа (отсортированные по возрастанию):")
    print(result)