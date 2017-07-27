import json


# El original es el que esta con minusculas y se compara con el de mayusculas que salio del csv
with open('essentials_original.json', encoding='utf-8') as data_file:
    data = json.load(data_file)

with open('essentials_csv.json', encoding='utf-8') as data_file:
    data_ = json.load(data_file)

d_original = data['items']
d_bueno = data_['items']

for i in range(len(data['items'])):
    for key, value in d_original[i].items():
        if d_original[i][key] != d_bueno[i][key]:
            d_original[i][key] = d_bueno[i].get(key)

print(d_original)


