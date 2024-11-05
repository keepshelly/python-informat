def luhn_check(card_number):
    digits = [int(d) for d in str(card_number)][::-1]
    total_sum = 0
    for i, digit in enumerate(digits):
        if i % 2 == 0:
            total_sum += digit
        else:
            doubled = digit * 2
            total_sum += doubled if doubled < 10 else doubled - 9
    return total_sum % 10 == 0
card_number = input("Введите номер карты для проверки: ")
if luhn_check(card_number):
    print("Номер карты корректен.")
else:
    print("Номер карты некорректен.")
