n = int(input())
while n > 10:
    n = sum(map(int, list(str(n))))
print(n)