a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))

if (a < b):
    if (a < c):
        print(f"Минимальное число: {a}")
    else:
        print(f"Минимальное число: {c}")
elif (b < c):
    print(f"Минимальное число: {b}")
else:
    print(f"Минимальное число: {c}")
