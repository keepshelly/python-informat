def abbreviate(word):
    if len(word) > 10:
        return f"{word[0]}{len(word) - 2}{word[-1]}"
    else:
        return word

n = int(input("Введите количество слов: "))
words = [input("Введите слово: ") for _ in range(n)]

abbreviated_words = [abbreviate(word) for word in words]

for word in abbreviated_words:
    print(word)
