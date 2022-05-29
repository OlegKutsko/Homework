x=float(input("Введите первое число: "))
y=float(input("Введите второе число: "))
z=input("Введите оператор (+, -, /, *): ")
if z=='+':
    result=x+y
elif z=='-':
    result=x-y
elif z=='*':
    result=round(x*y, 2)
elif z=='/' :
    if y!=0:
        result=round(x/y,2)
    elif y==0:
        result="Деление на 0!"
print("Результат вычислений: ",result)
