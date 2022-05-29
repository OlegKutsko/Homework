number = int(input("Введите число: "))
def fibonacci(number):
    a, b = 1, 1
    for i in range(number):
        yield a
        a, b = b, a + b
print(list(fibonacci(number)))