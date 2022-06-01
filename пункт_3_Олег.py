string = str(input("Введите отрывок текста: "))
unique_string = list(set(string))
unique_string.remove(' ')
counter = []
for letter in unique_string:
    counter.append(string.count(letter))

result = dict(zip(unique_string, counter))
reversed_dict = {}
reversed_keys = sorted(result, key=result.get, reverse=True)
for n in reversed_keys:
    reversed_dict[n] = result[n]
print(reversed_dict)
print(reversed_dict.values())