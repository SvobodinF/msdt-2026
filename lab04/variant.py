n = int(input("Введите количество чисел: "))

count = 0
sum = 0

for i in range(n):
    number = int(input(f"Введите число {i + 1}: "))

    if number % 3 != 0:
        count += 1
        sum += number

print(f"Количество чисел: {count}")
print(f"Сумма чисел: {sum}")