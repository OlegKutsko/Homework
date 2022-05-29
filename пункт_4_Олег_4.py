def fill_list(x: int, y: int, z: int, d: list):
    from random import randint
    for i in range(z):
        d.append(randint(x, y))


def calculations(random_list: list, result_dict: dict):
    for i in random_list:
        if i in result_dict:
            result_dict[i] += 1
        else:
            result_dict[i] = 1


lst = []
dct = {}
mn = int(input('От какого числа: '))
mx = int(input('До какого числа: '))
qty = int(input('Количество элементов: '))
fill_list(mn, mx, qty, lst)
calculations(lst, dct)

for item in sorted(dct):
    print("'%d':%d" % (item, dct[item]))