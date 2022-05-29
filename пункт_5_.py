string = input('Введите строку:')
s= string[1: len(string)-1]
if len(string)>2:
    print(s)
else:
    print('Ошибка')