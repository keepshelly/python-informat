n = int(input("Введите количество комнат: "))
available_rooms = 0

for _ in range(n):
    p, q = map(int, input("Введите количество людей и максимальное число мест в комнате: ").split())
    if q - p >= 2:
        available_rooms += 1
print("Количество подходящих комнат:", available_rooms)

