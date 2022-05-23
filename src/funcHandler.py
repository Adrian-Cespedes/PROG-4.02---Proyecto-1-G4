from functions.selectASCII import selectASCII
from functions.printASCII import printASCII

def showASCII():
    ascii = selectASCII()
    printASCII(ascii)

def rotate90():
    ascii = selectASCII()
    pass

def rotate90Anti():
    ascii = selectASCII()
    pass

def rotate180():
    ascii = selectASCII()
    for f in range(len(ascii)-1,-1,-1):
        for c in range(len(ascii[f])):
            print(ascii[f][c],end="")
        print()

def rotate180Anti():
    ascii = selectASCII()
    for f in range(len(ascii)-1,-1,-1):
        for c in range(len(ascii[f])-1,-1,-1):
            print(ascii[f][c],end="")
        print()

def frecChars():
    ascii = selectASCII()
    
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

def titulo():
    f = open("Assets/tittle.txt", 'r', encoding="utf8")
    print()
    print(''.join([line for line in f]))
    print("{:^100s}".format("Grupo 4"))