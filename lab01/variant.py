orderTitle = input("Введите название заказа: ")
customerName = input("Введите имя заказчика: ")

item1Name = input("Введите название первой позиции: ")
item1Quantity = int(input(f"Введите количество позиции \"{item1Name}\": "))
item1Price = float(input(f"Введите цену за единицу позиции \"{item1Name}\" в рублях: "))

item2Name = input("Введите название второй позиции: ")
item2Quantity = int(input(f"Введите количество позиции \"{item2Name}\": "))
item2Price = float(input(f"Введите цену за единицу позиции \"{item2Name}\" в рублях: "))

deliveryCost = float(input("Введите стоимость доставки в рублях: "))
paidAmount = float(input("Введите внесённую сумму в рублях: "))

item1Cost = item1Quantity * item1Price
item2Cost = item2Quantity * item2Price
itemsCost = item1Cost + item2Cost
totalCost = itemsCost + deliveryCost
totalQuantity = item1Quantity + item2Quantity
change = paidAmount - totalCost

print(f"\nЗаказ: {orderTitle}")
print(f"Заказчик: {customerName}")
print(f"{item1Name} | {item1Quantity} | {item1Price:.2f} | {item1Cost:.2f}")
print(f"{item2Name} | {item2Quantity} | {item2Price:.2f} | {item2Cost:.2f}")
print("Стоимость товаров без доставки:", f"{itemsCost:.2f}")
print("Стоимость доставки:", f"{deliveryCost:.2f}")
print("Итого с доставкой:", f"{totalCost:.2f}")
print("Общее количество единиц:", totalQuantity)
print("Сдача:", f"{change:.2f}")
