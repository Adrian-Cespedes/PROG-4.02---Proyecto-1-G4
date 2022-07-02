#
# 
# 

from functions.selectASCII import selectASCII
from functions.printASCII import printASCII
from functions.imports.loader import loadText
from os import listdir, system

"""
Funcion para cargar a memoria los ASCII's predefinidos y los asigna a la variable
ASCIIdir para su uso y modificacion.
"""
def loadToMemory():
    return {txt: loadText("Assets/" + txt) for txt in listdir("Assets") if not txt.startswith("#")}
ASCIIdir = loadToMemory()

"""
showASCII llama a la funcion selectASCII, la cual retorna un ASCII Art
en formato matriz.                                                          <-- TODAS LAS FUNCIONES HACEN ESTO
Luego se llama a la funcion printASCII, la cual imprime el ASCII para
su visualizacion.
"""
def showASCII():
    ascii = selectASCII(ASCIIdir)
    printASCII(ascii)


"""
Rota la matriz 90° horario conteniendo el ASCII Art siguiendo la siguiente logica:
- Todo elemento del mismo indice de columna (izq. a der.), se convierte
  en fila (descendente).
"""
def rotate90():
    ascii = selectASCII(ASCIIdir)
    new_ascii = list()

    for row in range(0, len(ascii[0])-1, 1):
        newRow = []
        for col in range(len(ascii)-1, -1, -1):
            newRow.append(ascii[col][row])
        new_ascii.append(newRow)

    printASCII(new_ascii)
    return new_ascii


"""
Rota la matriz 90° anti-horario siguiendo la misma logica del horario,
solo que se invierten los steps para obtener el resultado anti-horario.
"""
def rotate90Anti():
    ascii = selectASCII(ASCIIdir)
    new_ascii = list()

    for row in range(len(ascii[0])-1, -1, -1):
        newRow = []
        for col in range(0, len(ascii)-1, 1):
            newRow.append(ascii[col][row])
        new_ascii.append(newRow)

    printASCII(new_ascii)
    return new_ascii


"""
Rota la matriz 180° horario conteniendo el ASCII Art siguiendo la siguiente logica:
- Cada fila (ascendente) se vuelve su orden opuesto (ej: matriz[0] -> matriz[-1]),
  pero sus elementos se invierten de orden.
"""
def rotate180():
    ascii = selectASCII(ASCIIdir)
    new_ascii = list()

    for row in range(len(ascii)-1,-1,-1):
        newRow = []
        for col in range(len(ascii[row])-1,-1,-1):
            newRow.append(ascii[row][col])
        new_ascii.append(newRow)

    printASCII(new_ascii)
    return new_ascii


"""
Rotar 180° de forma horaria o anti-horaria resulta en la misma imagen.
"""
def rotate180Anti():
    ascii = selectASCII(ASCIIdir)
    new_ascii = list()

    for row in range(len(ascii)-1,-1,-1):
        newRow = []
        for col in range(len(ascii[row])-1,-1,-1):
            newRow.append(ascii[row][col])
        new_ascii.append(newRow)

    printASCII(new_ascii)
    return new_ascii


"""
Itera sobre los caracteres de la matriz y crea un diccionario para
llevar la cuenta de cada uno.
"""
def frecChars():
    ascii = selectASCII(ASCIIdir)
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
    art = selectASCII(ASCIIdir)
    result=list()
    for y in range(len(art)):
        linea=list()
        for x in range(len(art[0])-1, -1,-1):
            linea.append(art[y][x])
        result.append(linea)
    
    printASCII(result)
    return result

"""
Permite abrir un .txt de la carpeta "Customs" y la almacena en
memoria para su posterior uso dentro del programa.
"""
def readTxt():
    while True:
        try:
            name = input("Nombre del archivo: ")
            ascii = loadText("Customs/" + name)
            ASCIIdir[name] = ascii
            print()
            printASCII(ascii)
        except IOError:
            print("Archivo no encontrado...")
            continue
        break

"""
Funcion que contiene un sub-menu para poder seleccionar un ASCII en memoria, modificarlo
y guardar la modificacion como un nuevo .txt en ./Customs.
"""
def saveTxt():
    def clear():
        system("cls")

    def saveMenu():
        print("="*100)
        print("[1] Rotar 90 grados en sentido horario")
        print("[2] Rotar 90 grados en sentido anti-horario")
        print("[3] Rotar 180 grados en sentido horario")
        print("[4] Rotar 180 grados en sentido anti-horario")
        print("[5] Efecto espejo")
        print("="*100)
    
    def save(m):
        ask = "\nIngrese nombre para guardar (.txt): "
        with open("Customs/" + input(ask), "w", encoding="utf8") as f:
                for row in m:
                    row = "\n" + "".join(row)
                    f.write(row)

    while True:
        saveMenu()
        try:
            opcion = int(input("\nIngrese su opcion: "))
        except ValueError:
            clear()
            continue
        if opcion == 1:
            clear()
            ascii = rotate90()
            save(ascii)
            break
        elif opcion == 2:
            clear()
            ascii = rotate90Anti()
            save(ascii)
            break
        elif opcion == 3:
            clear()
            ascii = rotate180()
            save(ascii)
            break
        elif opcion == 4:
            clear()
            ascii = rotate180Anti()
            save(ascii)
            break
        elif opcion == 5:
            clear()
            ascii = mirrorASCII()
            save(ascii)
            break
        else:
            print("Escoge una de las opciones...")
            clear()
            continue

def titulo():
    f = open("Assets/#tittle.txt", 'r', encoding="utf8")
    print()
    print(''.join([line for line in f]))
    print("{:^100s}".format("Grupo 4"))
    f.close()