import re


def censor_text():
    try:
        with open('Tema7_sam4_input.txt', 'r', encoding='utf-8') as file:
            banned_words = file.read().split()
    except FileNotFoundError:
        print("Ошибка: файл Tema7_sam4_input.txt не найден")
        return

    banned_words.sort(key=len, reverse=True)

    sentence = input("Введите предложение: ")

    for word in banned_words:
        pattern = re.compile(re.escape(word), re.IGNORECASE)
        sentence = pattern.sub('*' * len(word), sentence)

    print("\nРезультат:")
    print(sentence)


if __name__ == "__main__":
    censor_text()