price = int(input("Введите цену товара: "))
count = int(input("Введите количество товара: "))
paid = int(input("Введите внесённую сумму: "))

total = price * count
change = paid - total
print(f"Общая стоимость: {total}")
print(f"Сдача: {change}")