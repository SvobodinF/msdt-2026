row_numbers = input("Введите числа через пробел: ").split()
conditionList = []

for row_number in row_numbers:
    number = int(row_number)
    if number % 3 != 0:
        conditionList.append(number)

print(f"Выборка {conditionList}")
print(f"Количество: {len(conditionList)}")
print(f"Сумма: {sum(conditionList)}")

sortedList = sorted(conditionList)
print(f"Отсортированое {sortedList}")