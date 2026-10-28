first_room = input("Введите первую аудиторию: ")
second_room = input("Введите вторую аудиторию: ")

print("Исходные:", first_room, second_room, sep=" ")

third_room = first_room
first_room = second_room
second_room = third_room

print("После обмена:", first_room, second_room, sep=" ")