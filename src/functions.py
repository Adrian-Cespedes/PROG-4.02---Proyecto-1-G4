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
    print()
    print("=" * 50)
    for txt in listaArt:
        print(f"\n[{n}] [{txt[1:]}]")
        n += 1
    print()
    print("=" * 50)
    opcion = int(input("\nEscoge un ASCII Art:"))
    while not opcion < len(listaArt):
        n = 0
        print()
        print("=" * 50)
        for txt in listaArt:
            print(f"\n[{n}] [{txt[1:]}]")
            n += 1
        print()
        print("=" * 50)
        opcion = int(input("\nEscoge un ASCII Art:"))
    path = "Assets/" + listaArt[opcion]
    print()
    return loadText(path)

def mostrarASCII():
    ascii = escogerASCII()
    imprimirASCII(ascii)

def rotar90():
    ascii = escogerASCII()
    pass

def rotar90Anti():
    ascii = escogerASCII()
    pass

def rotar180():
    ascii = escogerASCII()
    print("Ga")
    pass

def rotar180Anti():
    ascii = escogerASCII()
    pass

def frecCaracteres():
    ascii = escogerASCII()
    
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