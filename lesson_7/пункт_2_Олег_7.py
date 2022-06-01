file = open('article.txt')

lines = 0
words = 0
letters = 0

for line in file:
    lines += 1
    words += len(line.split())
    letters += len(line.strip('\n'))

print("Количество строк:", lines)
print("Количество слов:", words)
print("Количество букв:", letters)
