import json

with open('data.json', 'w') as file:
    json.dump({
    "firstName":"Alex",
    "lastName":"Richardson",
    "gender":"male"
    } , file)

s = {'age':33, 'city':'Minsk'}

with open('data.json', "r") as file:
    data = json.load(file)
data.update(s)

with open('data.json', "w") as file:
    json.dump(data, file)