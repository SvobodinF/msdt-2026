text = input("Введите строку: ")
length = len(text)

words = text.split()
normalized = " ".join(words)
newLength = len(normalized)

print(f"Исходная длина: {length}")
print(f"Новая длина: {newLength}")
print(f"Нормализованный текст: {normalized}")
print(f"Количество слов: {len(words)}")
