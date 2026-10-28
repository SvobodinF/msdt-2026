a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

step = 1 if a <= b else -1

for number in range(a, b + step, step):
    print(number)