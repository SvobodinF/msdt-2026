numbers = [int(part) for part in input("Введите числа через пробел: ").split()]
transformed = []

for item in numbers:
    transformed.append(abs(item))

print(numbers)
print(transformed)
