words = input("Введите строку: ").lower().split()
str = "".join(words)

if (len(str) == 0):
    print("Нет текста")
    exit()

if str == str[::-1]:
    print("Палиндром")
else:
    print("Не палиндром")


print("Проверка через цикл при помощи указателей")
pointer1 = 0
pointer2 = len(str) - 1

while pointer1 < pointer2:
    if str[pointer1] != str[pointer2]:
        print("Не палиндром")
        exit()
    pointer1 += 1
    pointer2 -= 1

print("Палиндром")