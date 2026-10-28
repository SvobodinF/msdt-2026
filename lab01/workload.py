subject1 = input("Введите название первого предмета: ")
count1 = int(input(f"Введите количество занятий по предмету \"{subject1}\" за неделю: "))
if count1 < 0:
    print("Количество занятий не может быть отрицательным")
    exit()
duration1 = int(input(f"Введите продолжительность одного занятия по предмету \"{subject1}\" в минутах: "))
if duration1 <= 0:
    print("Продолжительность занятия должна быть положительной")
    exit()

subject2 = input("Введите название второго предмета: ")
count2 = int(input(f"Введите количество занятий по предмету \"{subject2}\" за неделю: "))
if count2 < 0:
    print("Количество занятий не может быть отрицательным")
    exit()
duration2 = int(input(f"Введите продолжительность одного занятия по предмету \"{subject2}\" в минутах: "))
if duration2 <= 0:
    print("Продолжительность занятия должна быть положительной")
    exit()

time1 = count1 * duration1
time2 = count2 * duration2
totalMinutes = time1 + time2
totalHours = totalMinutes / 60

availableHours = float(input("Введите доступное время на неделю в часах: "))
if availableHours < totalHours:
    print("Доступного времени недостаточно для указанной нагрузки")
    exit()

freeHours = availableHours - totalHours

print(f"\nВремя на \"{subject1}\":", time1, "минут")
print(f"Время на \"{subject2}\":", time2, "минут")
print("Общая нагрузка:", totalMinutes, "минут")
print("Общая нагрузка:", f"{totalHours:.2f}", "часов")
print("Остаток свободного времени:", f"{freeHours:.2f}", "часов")
print("Нагрузка за 4 недели:", totalMinutes * 4, "минут")
print("Нагрузка за 4 недели:", f"{totalHours * 4:.2f}", "часов")
