name = input("Введите ваше имя: ")
with open("Tema7_sam5_hello.txt", "w", encoding="utf-8") as file:
    file.write(f"Привет, {name}! Рады видеть вас.")
print("Приветствие сохранено в файл Tema7_sam5_hello.txt")