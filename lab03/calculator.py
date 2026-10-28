val1 = float(input("Введите первое число: "))
val2 = float(input("Введите второе число: "))
operation = input("Введите операцию: ")

if operation == "+":
    print(f"Результат: {val1 + val2:.2f}")
elif operation == "-":
    print(f"Результат: {val1 - val2:.2f}")
elif operation == "*":
    print(f"Результат: {val1 * val2:.2f}")
elif operation == "/":
    if val2 != 0:
        print(f"Результат: {val1 / val2:.2f}")
    else:
        print("Деление на ноль запрещено")
else:
    print("Неизвестная операция")