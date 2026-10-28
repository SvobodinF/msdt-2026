total = int(input("Введите количество саженцев: "))
capacity = int(input("Введите количество саженцев в ряду: "))

fullRows = total // capacity
remainder = total % capacity
minRows = (total + capacity - 1) // capacity

print(f"Полных рядов: {fullRows}")
print(f"Остаток: {remainder}")
print(f"Минимальное количество рядов: {minRows}")
