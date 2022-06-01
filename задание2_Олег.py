#Первый пункт
sequence_of_numbers = input("Введите последовательность чисел через запятую:")
print(list(sequence_of_numbers.replace(',','')))
print(tuple(sequence_of_numbers.replace(',','')))
#Второй пункт
number = int(input("Введите число: "))
if (number%2 == 0):
  print("Четное число")
else:
  print("Нечетное число")
#Третий пункт
word = input('Введите слово:')
if str(word) == str(word)[::-1] :
    print("Результат: палиндром")
else:
    print("Результат: не палиндром")
#Четвертый пункт
x = input('Введите первое число:')
y = input('Введите второе число:')
c = x
x=y
y=c
print(x,y)
#Пятый пункт
string = input('Введите строку:')
if len(string)>2:
    def remove_char(s):
        result = s[1: -1]
        return result


    print(remove_char(string))
else:
    print('Ошибка')