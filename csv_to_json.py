import pandas as pd
import json
import pprint
import io


def csv_to_json(archivo):
    """
    Esta funcion toma como argumento el nombre del archivo con la extension .csv y lo pasa a formato .json
    clasificandolos por la columna Topic
    :param archivo: nombre del archivo
    """
    df = pd.read_csv(archivo)
    topics = list(df['Topic'].unique())
    topics = [x for x in topics if str(x) != 'nan']

    for topic in topics:
        df_ = df[df['Topic'] == topic]

        df_ = df_[['Spanish', 'English', 'French', 'Chinese', 'EnglishAudio', 'SpanishAudio', 'frenchaudio',
                   'chineseaudio', 'Image']]

        df_ = df_.to_json(orient='records')
        data_json = json.loads(df_)
        pprint.pprint(data_json)
        print(topic)

        with io.open('{}.json'.format(topic), 'w', encoding='utf-8') as f:
            f.write(json.dumps(data_json, ensure_ascii=False, indent=4, sort_keys=True))

if __name__ == '__main__':
    csv_to_json('Oasis.csv')
