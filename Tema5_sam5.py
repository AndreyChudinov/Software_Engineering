from collections import Counter

def process_list(lst):
    counts = Counter(lst)
    result = set()
    for num, count in counts.items():
        result.add(num)
        for k in range(2, count + 1):
            result.add(str(num) * k)
    return result

list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

print(process_list(list_1))
print(process_list(list_2))
print(process_list(list_3))