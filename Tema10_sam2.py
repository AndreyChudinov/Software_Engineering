class EmptyFileError(Exception):
    pass

def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            if not content.strip():
                raise EmptyFileError("файл пустой")
            return content
    except FileNotFoundError:
        return "Файл не найден"
    except EmptyFileError as e:
        return str(e)
    except Exception as e:
        return f"Произошла ошибка: {e}"

print("Пустой файл:")
result1 = read_file("Tema10_sam2_empty.txt")
print(result1)

print("\nФайл с данными:")
result2 = read_file("Tema10_sam2_data.txt")
print(result2)