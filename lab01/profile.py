surname = input("Введите вашу фамилию: ")
name = input("Введите ваше имя: ")
group = input("Введите вашу группу: ")
city = input("Введите ваш город: ")
age = int(input("Введите ваш возраст: "))

if (age <= 0 or age > 120):
    print("Некорректный возраст")
    exit()

subject = input("Введите ваш предмет: ")
hoursPerWeek = float(input("Введите количество часов в неделю: "))

print("\nКарточка:")
print("Имя и фамилия:", name, surname)
print("Возраст через 4 года:", age + 4)
print("Время подготовки за 4 недели", f"{hoursPerWeek * 4:.2f}")
print("avg hours per day:", f"{hoursPerWeek / 7:.2f}")