def analyze_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    lines = len(text.splitlines())

    words = len(text.split())

    letters = 0
    for char in text:
        if 'a' <= char.lower() <= 'z':
            letters += 1

    return letters, words, lines


letters, words, lines = analyze_text("Tema7_sam3_input.txt")

print("Input file contains:")
print(f"{letters} letters")
print(f"{words} words")
print(f"{lines} lines")