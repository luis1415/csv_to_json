import pandas as pd
import json
from pprint import pprint


def json_to_csv(archivo_csv, archivo_json, indice='items'):
    with open(archivo_json, encoding='utf-8') as data_file:
        data = json.load(data_file)

    pprint(data[indice])
    df = pd.DataFrame(data[indice])
    df.to_csv(archivo_csv, index=False)

if __name__ == '__main__':
    json_to_csv('Essentials.csv', 'Essentials.json')
