#
# 
# 

from functions.selectASCII import selectASCII
from functions.printASCII import printASCII

def showASCII():
    ascii = selectASCII()
    printASCII(ascii)

def rotate90():
    ascii = selectASCII()
    new_ascii = list()

    for row in range(0, len(ascii[0])-1, 1):
        newRow = []
        for col in range(len(ascii)-1, -1, -1):
            newRow.append(ascii[col][row])
        new_ascii.append(newRow)

    printASCII(new_ascii)

def rotate90Anti():
    ascii = selectASCII()
    new_ascii = list()

    for row in range(len(ascii[0])-1, -1, -1):
        newRow = []
        for col in range(0, len(ascii)-1, 1):
            newRow.append(ascii[col][row])
        new_ascii.append(newRow)

    printASCII(new_ascii)

def rotate180():                               #La funcion definida como rotate180 tiene como objetivo imprimir las filas desde la ultima hasta la primera, considerando las columnas iguales
    ascii = selectASCII()                      #A las que estaban en la imagen ASCII original
    new_ascii = list()

    for row in range(len(ascii)-1,-1,-1):
        newRow = []
        for col in range(len(ascii[row])):
            newRow.append(ascii[row][col])
        new_ascii.append(newRow)

    printASCII(new_ascii)

def rotate180Anti():                               #La funcion definida como rotate180Anti tiene como objetivo imprimir las filas desde la ultima hasta la primera y desde la ultima columna
    ascii = selectASCII()                          #Hasta la primera
    new_ascii = list()

    for row in range(len(ascii)-1,-1,-1):
        newRow = []
        for col in range(len(ascii[row])-1,-1,-1):
            newRow.append(ascii[row][col])
        new_ascii.append(newRow)

    printASCII(new_ascii)

def frecChars():
    # Selec ascii, tal como lo dice el nombre, solo selecciona el ascii para ser almacenado en la variable ascci
    ascii = selectASCII()
    
    # Se crea diccionario
    charsDic  = {}

    #Iteración sobre filas de matriz
    for row in ascii:
        #Interación sobre columnas de filas
        for x in row:
            #Si se encuentra marcado en el diccionario, sumar 1
            if x in charsDic:
                charsDic[x] += 1
            #De lo contrario inicializar con 1
            else:
                charsDic[x] = 1

    print("%-10s | %10s" % ("Caracter","Frecuencia"))
    print("¯" * 23)
    
    for key,value in charsDic.items():
        print("%-10s : %-s" % (key,value))

def mirrorASCII():
    art = selectASCII()
    result=list()
    #iterar desde la longitud hasta cero
    for y in range(len(art)):
        linea=list()
        for x in range(len(art[0])-1, -1,-1):
            linea.append(art[y][x])
        result.append(linea)
    
    printASCII(result)

# 'def titulo' como que nos abre paso a los asciis
def titulo():
    #Carga el logo del titulo desde el archivo tittle.txt
    f = open("Assets/tittle.txt", 'r', encoding="utf8")
    print()
    #Imprime el Titulo
    print(''.join([line for line in f]))
    print("{:^100s}".format("Grupo 4"))