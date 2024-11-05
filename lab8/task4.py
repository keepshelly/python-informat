def main():
    numbers = []
    while True:
        user_input = input("Введите число (или нажмите Enter для завершения): ")
        if user_input == "":
            break
        try:
            number = float(user_input)  
            numbers.append(number)
        except ValueError:
            print("Ошибка ввода. Пожалуйста, введите корректное число.")


    if numbers:

        average = sum(numbers) / len(numbers)
        print(f"\nСреднее значение: {average}")

        below_average = [num for num in numbers if num < average]
        equal_to_average = [num for num in numbers if num == average]
        above_average = [num for num in numbers if num > average]

        print("\nЧисла ниже среднего значения:")
        print(below_average if below_average else "Нет чисел ниже среднего")

        print("\nЧисла, равные среднему значению:")
        print(equal_to_average if equal_to_average else "Нет чисел, равных среднему")

        print("\nЧисла выше среднего значения:")
        print(above_average if above_average else "Нет чисел выше среднего")
    else:
        print("Вы не ввели ни одного числа.")

main()
