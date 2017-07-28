import json
import os
import pprint
import io

os.chdir('oasis')
lista_originales = os.listdir()
os.chdir('..')
print(lista_originales)
for arch in lista_originales:
    try:
        # El original es el que esta con minusculas y se compara con el de mayusculas que salio del csv
        with open(arch, encoding='utf-8') as data_file:
            data = json.load(data_file)

        with open('csv_{}'.format(arch), encoding='utf-8') as data_file:
            data_ = json.load(data_file)

        d_original = data['items']
        d_bueno = data_['items']

        for i in range(len(data['items'])):
                for key, value in d_original[i].items():
                    if key == 'chinese':
                        d_original[i][key] = d_bueno[i].get(key)
        d_original = {'items': d_original}
        with io.open('CORREGIDO_{}'.format(arch), 'w', encoding='utf-8') as f:
            f.write(json.dumps(d_original, ensure_ascii=False, indent=4, sort_keys=True))
        pprint.pprint(d_original)

    except:
        pass
