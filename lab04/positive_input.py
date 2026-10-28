attempts = 0
number = int(input("Введите число: "))

while number <= 0:
    attempts += 1
    number = int(input("Введите число: "))

print("Квадрат числа:", number ** 2)
print("Количество отклонённых попыток:", attempts)
