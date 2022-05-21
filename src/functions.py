from os import listdir
from loader import loadText

def titulo():
    f = open ("Assets/tittle.txt", 'r', encoding="utf8")
    print()
    print(''.join([line for line in f]))
    print("{:^100s}".format("Grupo 4"))

def imprimirASCII(mat):
    filas = len(mat)
    col   = len(mat[0])
    for f in range(filas):
        for c in range(col):
            print((mat[f][c]), end="")
        print()    

def escogerASCII():
    listaArt = listdir("Assets")
    for txt in listaArt:
        if not txt.startswith("#"):
            listaArt.remove(txt)
    n = 0
    for txt in listaArt:
        print(f"\n[{n}] [{txt[2:]}]")
        opcion = int(input("\nEscoge un ASCII Art:"))
        n += 1
    print(listaArt)
    path = "Assets/" + listaArt[opcion]
    imprimirASCII(loadText(path))

def mostrarASCII():
    ascii = escogerASCII()
    pass

def rotar90():
    ascii = escogerASCII()
    pass

def rotar90Anti():
    ascii = escogerASCII()
    pass

def rotar180():
    ascii = escogerASCII()
    pass

def rotar180Anti():
    ascii = escogerASCII()
    pass

def frecCaracteres():
    ascii = escogerASCII()
    pass