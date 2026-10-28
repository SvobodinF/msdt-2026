n = int(input("Введите количество чисел: "))

sum = 0
above_zero = 0
max = float('-inf')

for i in range(n):
    number = int(input(f"Введите число {i + 1}: "))
    sum += number
    if number > 0:
        above_zero += 1
    if number > max:
        max = number

print(f"Сумма чисел: {sum}")
print(f"Количество чисел больше нуля: {above_zero}")
print(f"Максимальное число: {max}")