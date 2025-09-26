value = 0
while value < 100:
    if value == 0:
        value += 10
    elif value // 5 > 1: #Изменено с >2 на >1 для предотвращения бесконечного цикла
        value *= 5
    else:
        value -= 5
    print(value)