from functions.selectASCII import selectASCII
from functions.printASCII import printASCII

def showASCII():
    ascii = selectASCII()
    printASCII(ascii)

def rotate90():
    ascii = selectASCII()
    for col in range(0, len(ascii[0])-1, 1):
        for fil in range(len(ascii)-1, -1, -1):
            print(ascii[fil][col], end='')
        print('')

def rotate90Anti():
    ascii = selectASCII()
    for col in range(len(ascii[0])-1, -1, -1):
        for fil in range(0, len(ascii)-1, 1):
            print(ascii[fil][col], end='')
        print('')

def rotate180():                               #La funcion definida como rotate180 tiene como objetivo imprimir las filas desde la ultima hasta la primera, considerando las columnas iguales
    ascii = selectASCII()                      #A las que estaban en la imagen ASCII original
    for f in range(len(ascii)-1,-1,-1):
        for c in range(len(ascii[f])):
            print(ascii[f][c],end="")
        print()

def rotate180Anti():                               #La funcion definida como rotate180Anti tiene como objetivo imprimir las filas desde la ultima hasta la primera y desde la ultima columna
    ascii = selectASCII()                          #Hasta la primera
    for f in range(len(ascii)-1,-1,-1):
        for c in range(len(ascii[f])-1,-1,-1):
            print(ascii[f][c],end="")
        print()

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

# 'def titulo' como que nos abre paso a los asciis
def titulo():
    #Carga el logo del titulo desde el archivo tittle.txt
    f = open("Assets/tittle.txt", 'r', encoding="utf8")
    print()
    #Imprime el Titulo
    print(''.join([line for line in f]))
    print("{:^100s}".format("Grupo 4"))