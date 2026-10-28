x = float(input("Введите координату x: "))
y = float(input("Введите координату y: "))

if (0 <= x and x <= 5) and (0 <= y and y <= 3):
    print("Внутри или на границе")
else:
    print("Снаружи")