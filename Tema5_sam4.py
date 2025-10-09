grades1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
grades2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
grades3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

def fix_grades(grades):
    return [4 if x == 3 else x for x in grades if x != 2]

print(f"Обновленный массив 1: {fix_grades(grades1)}")
print(f"Обновленный массив 2: {fix_grades(grades2)}")
print(f"Обновленный массив 3: {fix_grades(grades3)}")