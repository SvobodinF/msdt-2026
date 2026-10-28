str = input("Введите строку: ")

count = str.count(":")
print(f"Количество двоеточий: {count}")

str = str.replace(":", "-")
print(f"Строка после замены двоеточий на дефисы:\n{str}")