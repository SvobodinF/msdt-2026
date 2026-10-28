numbers = [int(part) for part in input("Введите числа через пробел: ").split()]

if len(numbers) == 0:
    print("Нет данных")
    exit()

max_number = max(numbers)
result = []

for index, value in enumerate(numbers):
    if value == max_number:
        result.append(index)

print(result)