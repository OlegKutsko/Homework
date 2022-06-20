import sys


def fibonacci(n):
    list=[0,1]
    a=0
    b=1
    for i in range(0,98,1):
        list.append(list[a]+list[b])
        a+=1
        b+=1
    return list

print(fibonacci(100))
print(sys.getsizeof(fibonacci(100)))


def fibonacci_gen(n):
    list=[0,1]
    a=0
    b=1
    for i in range(0,98,1):
        list.append(list[a]+list[b])
        a+=1
        b+=1
    yield list


print(sys.getsizeof(fibonacci_gen(100)))