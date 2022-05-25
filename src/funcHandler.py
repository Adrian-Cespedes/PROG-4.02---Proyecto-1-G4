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
    
    # Se crea listas
    charsInd =[]
    counterInd = []

    print("%-10s | %10s" % ("Caracter","Frecuencia"))
    print("¯" * 23)
    for row in ascii:
        for x in row:
            if not (x in charsInd):
                charsInd.append(x)
                counterInd.append(0)
                counterInd[charsInd.index(x)] += 1
            else:
                counterInd[charsInd.index(x)] += 1
    
    for i in range(len(charsInd)):
        print("%-10s : %-s" % (charsInd[i],counterInd[i]))

# 'def titulo' como que nos abre paso a los asciis
def titulo():
    f = open("Assets/tittle.txt", 'r', encoding="utf8")
    print()
# ¿?
    print(''.join([line for line in f]))
    print("{:^100s}".format("Grupo 4"))