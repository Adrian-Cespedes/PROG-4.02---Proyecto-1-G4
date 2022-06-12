#
# 
# 

from functions.selectASCII import selectASCII
from functions.printASCII import printASCII

"""
showASCII llama a la funcion selectASCII, la cual retorna un ASCII Art
en formato matriz.                                                          <-- TODAS LAS FUNCIONES HACEN ESTO
Luego se llama a la funcion printASCII, la cual imprime el ASCII para
su visualizacion.
"""
def showASCII():
    ascii = selectASCII()
    printASCII(ascii)


"""
Rota la matriz 90° horario conteniendo el ASCII Art siguiendo la siguiente logica:
- Todo elemento del mismo indice de columna (izq. a der.), se convierte
  en fila (descendente).
"""
def rotate90():
    ascii = selectASCII()
    new_ascii = list()

    for row in range(0, len(ascii[0])-1, 1):
        newRow = []
        for col in range(len(ascii)-1, -1, -1):
            newRow.append(ascii[col][row])
        new_ascii.append(newRow)

    printASCII(new_ascii)


"""
Rota la matriz 90° anti-horario siguiendo la misma logica del horario,
solo que se invierten los steps para obtener el resultado anti-horario.
"""
def rotate90Anti():
    ascii = selectASCII()
    new_ascii = list()

    for row in range(len(ascii[0])-1, -1, -1):
        newRow = []
        for col in range(0, len(ascii)-1, 1):
            newRow.append(ascii[col][row])
        new_ascii.append(newRow)

    printASCII(new_ascii)


"""
Rota la matriz 180° horario conteniendo el ASCII Art siguiendo la siguiente logica:
- Cada fila (ascendente) se vuelve su orden opuesto (ej: matriz[0] -> matriz[-1]),
  pero sus elementos se invierten de orden.
"""
def rotate180():
    ascii = selectASCII()
    new_ascii = list()

    for row in range(len(ascii)-1,-1,-1):
        newRow = []
        for col in range(len(ascii[row])-1,-1,-1):
            newRow.append(ascii[row][col])
        new_ascii.append(newRow)

    printASCII(new_ascii)


"""
Rotar 180° de forma horaria o anti-horaria resulta en la misma imagen.
"""
def rotate180Anti():
    ascii = selectASCII()
    new_ascii = list()

    for row in range(len(ascii)-1,-1,-1):
        newRow = []
        for col in range(len(ascii[row])-1,-1,-1):
            newRow.append(ascii[row][col])
        new_ascii.append(newRow)

    printASCII(new_ascii)


"""
Itera sobre los caracteres de la matriz y crea un diccionario para
llevar la cuenta de cada uno.
"""
def frecChars():
    ascii = selectASCII()
    charsDic  = {}

    for row in ascii:
        for x in row:
            if x in charsDic:
                charsDic[x] += 1
            else:
                charsDic[x] = 1

    print("%-10s | %10s" % ("Caracter","Frecuencia"))
    print("¯" * 23)
    
    for key,value in charsDic.items():
        print("%-10s : %-s" % (key,value))


"""
Hace un efecto espejo al ASCII Art siguien la siguiente logica:
- La matriz es la misma, pero los ordenes/indices de los elementos
  de cada fila se invierten.
"""
def mirrorASCII():
    art = selectASCII()
    result=list()
    for y in range(len(art)):
        linea=list()
        for x in range(len(art[0])-1, -1,-1):
            linea.append(art[y][x])
        result.append(linea)
    
    printASCII(result)

def titulo():
    f = open("Assets/tittle.txt", 'r', encoding="utf8")
    print()
    print(''.join([line for line in f]))
    print("{:^100s}".format("Grupo 4"))