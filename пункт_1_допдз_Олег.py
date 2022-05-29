from sympy import *
number = int(input("Введите число от 1 до 1000: "))
if number in range(1, 1000):
    print(isprime(number))
else:
    print("Ошибка")