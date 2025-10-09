import math

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

max_sides = [max(one), max(two), max(three)]
min_sides = [min(one), min(two), min(three)]

def calculate_area(sides):
    """Вычисляет площадь треугольника по формуле Герона"""
    a, b, c = sorted(sides)
    if a + b <= c:
        return None
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

max_area = calculate_area(max_sides)
min_area = calculate_area(min_sides)

print(f"Площадь треугольника из максимальных элементов: {max_area:.2f}")
print(f"Площадь треугольника из минимальных элементов: {min_area:.2f}")