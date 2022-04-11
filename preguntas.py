"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

def sum_of_list (l):
    total = 0
    for val in l:
        total = total + val
    return total

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    with open('data.csv', "r") as file:
        data = file.readlines()
    #Limpieza

    #Eliminar el retorno de carro
    data = [line.replace('\n', '') for line in data]

    #Quitar el espacio en blanco y cambairlo por ','
    data = [line.replace('\t', ',') for line in data]

    #Crear lista
    data = [line.split(',') for line in data] 

    #Extraer la columna 2 de la lista dentro de la lista
    data_col_2 = [data[i][1] for i in  range(len(data))]

    # Volver los valores de la lista números
    num_col_2 = list(map(int, data_col_2))

    suma = sum_of_list(num_col_2)

    return suma


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    with open('data.csv', "r") as file:
        data = file.readlines()
        #Limpieza
    
    #Eliminar el retorno de carro
    data = [line.replace('\n', '') for line in data]

    #Quitar el espacio en blanco y cambairlo por ','
    data = [line.replace('\t', ',') for line in data]
    #Extraer la columna 1 en una nueva lista 

    data_col_1 = [i[0] for i in data [0:]]

    list_ = {}

    #usar get para contar elementos. 
    # Al llamar get de esta manera obtengo el recuento actual de una letra dada o 0 (valor predetermiando)

    for letter in data_col_1:
        list_[letter] = list_.get(letter, 0) + 1

    list_num = sorted(list_.items())
    return list_num


from operator import itemgetter
#Convertir la Tupla en un diccionario dentro de un diccionario
def Convert(tup, di):
    for a, b in tup:
        di.setdefault(a, []).append(b)
    return di

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    with open('data.csv', "r") as file:
        data = file.readlines()
    #Limpieza
    
    #Eliminar el retorno de carro
    data = [line.replace('\n', '') for line in data]

    #Quitar el espacio en blanco y cambairlo por ','
    data = [line.replace('\t', ',') for line in data]

    data = [line.split(',') for line in data]

    #Extraer la columna 1 y 2 en una nueva lista 

    col_2 = [data[i][:2] for i in  range(len(data))]

    # Volver los valores de la lista números
    for line in range(len(col_2)):
        col_2[line][1] = int(col_2[line][1])

    #Volver la lista en tupla
    my_tuple = [tuple (l) for l in col_2]

    my_dict = {}

    Convert(my_tuple, my_dict)

    sum_dict = {k:sum(i) for k, i in my_dict.items()}

    list_of_tuples = [(k,v) for k, v in sum_dict.items()]

    list_of_tuples = sorted(list_of_tuples, key = itemgetter(0), reverse=False)

     
    return list_of_tuples   

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    with open('data.csv', "r") as file:
        data = file.readlines()

    #Eliminar el retorno de carro
    data = [line.replace('\n', '') for line in data]

    #Quitar el espacio en blanco y cambairlo por ','
    data = [line.replace('\t', ',') for line in data]

    #crear lista
    data = [line.split(',') for line in data]

    #extraer filas de fechas
    fechas = [data[i][2] for i in range(len(data))]
    mes = [fechas[i][5:7] for i in range(len(data)) ]

    list_ = {}

    #usar get para contar elementos. 
    # Al llamar get de esta manera obtengo el recuento actual de una letra dada o 0 (valor predetermiando)

    for M in mes:
        list_[M] = list_.get(M, 0) + 1

    list_num = sorted(list_.items())
    
    return list_num

from operator import itemgetter

def Convert(tup, di):
    for a, b in tup:
        di.setdefault(a, []).append(b)
    return di

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    with open('data.csv', "r") as file:
        data = file.readlines()
        #Limpieza
        
    #Eliminar el retorno de carro
    data = [line.replace('\n', '') for line in data]

    #Quitar el espacio en blanco y cambairlo por ','
    data = [line.replace('\t', ',') for line in data]

    data = [line.split(',') for line in data]

    #Extraer la columna 1 y 2 en una nueva lista 

    col_2 = [data[i][:2] for i in  range(len(data))]

    # Volver los valores de la lista en int
    for line in range(len(col_2)):
        col_2[line][1] = int(col_2[line][1])

    #Volver la lista en tupla
    my_tuple = [tuple (col_2) for col_2 in col_2]

    my_dict = {}

    Convert(my_tuple, my_dict)

    dic_max = {k:max(i) for k, i in my_dict.items()}
    dic_min = {k:min(i) for k, i in my_dict.items()}

    def mergeDict(dict_1, dict_2):
        new_dict = {**dict_2, **dict_1}
        for key, value in new_dict.items():
            if key in dict_1 and key in dict_2:
                new_dict[key] = [value , dict_2[key]]
        return new_dict

    new_dict = mergeDict(dic_max, dic_min)

    # Volver los valores de la lista en tupla
    for k, v in new_dict.items():
        new_dict[k] = tuple(v)

    list_of_tuples = [(k,v) for (k, v) in new_dict.items()]
    #Quitar la tupla dentro de la tupla
    list_good = [(x, y, z) for x, (y, z) in list_of_tuples]

    list_good = sorted(list_good, key = itemgetter(0), reverse=False)

    return list_good


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    return


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    return


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    return


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    return


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    return


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    return


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    return
