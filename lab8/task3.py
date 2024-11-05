numbers = [1, 3, 2, 4, 3, 5, 7, 6]
result = [numbers[i] for i in range(1, len(numbers)) if numbers[i] > numbers[i - 1]]
print("Элементы, которые больше предыдущего:", result)
