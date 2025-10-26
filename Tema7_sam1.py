import string
from collections import Counter


def analyze_text(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read().lower()

        text = text.translate(str.maketrans('', '', string.punctuation))

        words = text.split()
        total_words = len(words)

        if total_words == 0:
            print("Файл пустой или не содержит слов.")
            return

        word_counts = Counter(words)
        most_common_word, frequency = word_counts.most_common(1)[0]

        print(f"Общее количество слов в файле: {total_words}")
        print(f"Самое часто встречающееся слово: '{most_common_word}' (встречается {frequency} раз)")

    except FileNotFoundError:
        print(f"Ошибка: файл '{file_path}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    analyze_text("C:/Users/ЛилияАндрей/Desktop/Test.txt")