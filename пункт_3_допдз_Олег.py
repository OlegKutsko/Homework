a = list(input("Введите первый список: "))
b = list(input("Введите второй список: "))

print(sorted(set(a) - set(b)))