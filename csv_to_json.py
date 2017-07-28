import pandas as pd
import json
import pprint
import io


def csv_to_json(archivo, clase, columnas):
    """
    Esta funcion toma como argumento el nombre del archivo con la extension .csv y lo pasa a formato .json
    clasificandolos y sacando un archivo por la columna clase
    :param archivo: nombre del archivo
    :param clase: la columna del csv por la cual se clasifican los archivos
    :param columnas: las columnas que se filtran en el dataframe
    """
    df = pd.read_csv(archivo)
    topics = list(df[clase].unique())
    topics = [x for x in topics if str(x) != 'nan']

    for topic in topics:
        df_ = df[df[clase] == topic]

        df_ = df_[columnas]
        df_.columns = ['spanish', 'english', 'french', 'chinese', 'englishaudio', 'spanishaudio', 'frenchaudio',
                       'chineseaudio', 'image']
        print(df_.columns)
        df_ = df_.to_json(orient='records')
        data_json = json.loads(df_)
        pprint.pprint(data_json[0])
        data_json = {'items': data_json}
        print(topic)

        with io.open('csv_{}.json'.format(topic.lower()), 'w', encoding='utf-8') as f:
            f.write(json.dumps(data_json, ensure_ascii=False, indent=4, sort_keys=True))


if __name__ == '__main__':
    # para el primer archivo de oasis
    columnas_oasis = ['Spanish', 'English', 'French', 'Chinese', 'EnglishAudio', 'SpanishAudio', 'frenchaudio',
                      'chineseaudio', 'Image']
    csv_to_json('Oasis.csv', 'Topic', columnas_oasis)

    # para las lecciones
    columnas_lessons = ['Spanish', 'English', 'French', 'Chinese', 'SpanishAudio', 'EnglishAudio',
                        'FrenchAudio', 'ChineseAudio', 'Image']
    csv_to_json('lesson1.csv', 'Lesson ID', columnas_lessons)
    csv_to_json('lesson2.csv', 'Lesson ID', columnas_lessons)
    csv_to_json('lesson3.csv', 'Lesson ID', columnas_lessons)


