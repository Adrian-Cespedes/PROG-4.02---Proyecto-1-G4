from os import listdir
from functions.imports.loader import loadText

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