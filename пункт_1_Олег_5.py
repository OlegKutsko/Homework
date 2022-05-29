from datetime import datetime


def benchmark(func: any)-> any:
    def timeit():
        begin = datetime.now()
        func()
        res = datetime.now() - begin
        print(res)
    return timeit


@benchmark
def set_0(start=0,end=100000):
    set_1 = set()
    for i in range(start, end+1):
        set_1.add(i)
    1 in set_1
    set_1.remove(3)
    return set_1


@benchmark
def list_0(start=0,end=100000):
    list_1 = list()
    for i in range(start, end+1):
        list_1.append(i)
    1 in list_1
    list_1.remove(3)
    return list_1


set_0()
list_0()
