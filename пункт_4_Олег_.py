num = int(input("Введите число: "))
sum = 0
temp = num
while temp > 0:
      digit = temp % 10
      sum += digit ** len(str(num))
      temp //= 10
if num == sum:
      print(num,"- число нарцисс")
else:
      print(num,"- не число нарцисс")
