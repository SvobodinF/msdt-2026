percent = int(input("Введите процент: "))

if (percent < 0 or percent > 100):
    print("Ошибка диапазона")
    exit()

if (percent >= 0 and percent <= 9):
    print("Начало")
elif (percent >= 10 and percent <= 89):
    print("Чтение")
elif (percent >= 90 and percent <= 100):
    print("Почти готово")