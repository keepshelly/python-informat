heights = list(map(int, input("Введите рост людей в строю (через пробел): ").split()))
andrey_height = int(input("Введите рост Андрея: "))
position = 1 
for height in heights:
    if height < andrey_height:
        break
    position += 1

print("Андрей должен встать на позицию:", position)
