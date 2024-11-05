data = ['a', 1, 'b', 2, 'c', 3, 'd', 4, 'e', 5]
letters = [item for item in data if isinstance(item, str)]
numbers = [item for item in data if isinstance(item, int)]
del data
print("Список с буквами:", letters)
print("Список с цифрами:", numbers)
