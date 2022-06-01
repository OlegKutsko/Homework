dictionary = {1: 1, 2: 15, 3: 7}
sorted_dict = {}
reversed_dict = {}
sorted_keys = sorted(dictionary, key=dictionary.get)
reversed_keys = sorted(dictionary, key=dictionary.get, reverse=True)

for w in sorted_keys:
    sorted_dict[w] = dictionary[w]
for n in reversed_keys:
    reversed_dict[n] = dictionary[n]

print(sorted_dict)
print(reversed_dict)