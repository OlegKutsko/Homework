x = int(input("введите первое число: "))
y = int(input("введите второе число: "))
list = []
for i in range(x, y+1):
    list.append(i)
cnt = 0
for i in range(x, y+1):
    if (i % 5 != 0):
        cnt += 1
print(list)
print(cnt)
