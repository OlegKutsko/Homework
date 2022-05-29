import math


def lcm(x: int, y: int) -> int:
    return int(x*y/math.gcd(x, y))


x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))
print(lcm(x,y))