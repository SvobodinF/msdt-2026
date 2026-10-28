text = input("Введите строку: ")
words = text.split()

count = 0

for word in words:
    word = word.strip(".,!?;:").lower()
    if word == "":
        continue
    if "р" in word:
        print(word)
        count += 1

if count == 0:
    print("Нет совпадений")

print(f"Количество: {count}")