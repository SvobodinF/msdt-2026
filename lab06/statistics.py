str = input("Введите числа через пробел: ")

if len(str) == 0:
    print("Нет данных")
    exit()

rowNumbers = str.split()

numbers = []
sum = 0
min = float('inf')
max = float('-inf')

for rowNumber in rowNumbers:
    number = int(rowNumber)
    sum += number

    if number < min:
        min = number
    if number > max:
        max = number

    numbers.append(number)

print(f"Количество: {len(numbers)}")
print(f"Сумма: {sum}")
print(f"Минимум: {min}")
print(f"Максимум: {max}")
print(f"Среднее: {sum/len(numbers):.2f}")