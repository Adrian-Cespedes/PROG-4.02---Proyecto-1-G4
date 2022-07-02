#
#
#

from os import system

def clear():
    system("cls")

"""
Muestra todas las opciones disponibles en memoria.
Cuando se obtiene una opcion valida, devuelve un string
conteniendo la matriz de la seleccion.

return: Ruta del ASCII en .txt en string
"""
def selectASCII(artList):
    while True:
        clear()

        n = 0
        print()
        print("=" * 50)

        for txt in artList:
            print(f"\n[{n}] [{txt}]")
            n += 1
        print()
        print("=" * 50)
        try:
            option = int(input("\nEscoge un ASCII Art: "))
        except ValueError:
            continue

        clear()
        try:
            ascii = artList[list(artList.keys())[option]]
        except:
            continue
        return ascii