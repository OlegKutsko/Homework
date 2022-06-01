def CalcSumNumbers(A: list) -> float:
    if A == []:
        return 0
    else:
        summ = CalcSumNumbers(A[1:])
        summ = summ + A[0]
        return summ


L = [ 1, 3, 10, 11, 23, 25]
summ = CalcSumNumbers(L)
print(summ)
