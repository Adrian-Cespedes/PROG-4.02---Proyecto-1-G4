#
#
#

from os import listdir, system
from functions.imports.loader import loadText

def clear():
    system("cls")

"""
Muestra todas las opciones disponibles.
Cuando se obtiene una opcion valida, se genera un string
conteniendo la direccion al archivo txt.

return: Ruta del ASCII en .txt en string
"""

def selectASCII():
    while True:
        clear()
        artList = listdir("Assets")

        for txt in artList:
            if not txt.startswith("#"):
                artList.remove(txt)
        n = 0
        print()
        print("=" * 50)

        for txt in artList:
            print(f"\n[{n}] [{txt[1:]}]")
            n += 1
        print()
        print("=" * 50)
        try:
            option = int(input("\nEscoge un ASCII Art: "))
        except ValueError:
            continue
        try:    
            path = "Assets/" + artList[option]
        except IndexError:
            continue

        print()
        return loadText(path)