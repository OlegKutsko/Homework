def sum_range(start:int, end: int) -> int:
    if start>end:
        start, end = end, start
    return float(sum(range(start, end+1)))


start = int(input("ведите первое число: "))
end = int(input("ведите второе число: "))
print(float(sum_range(start, end)))
