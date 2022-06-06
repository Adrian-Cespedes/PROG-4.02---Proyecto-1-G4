#
#
#

from os import listdir, system
from functions.imports.loader import loadText

def clear():
    system("cls")

# ¿Cual es os y el otro? creo que se cuales son pero mejor me explican con lujo de detalle

def selectASCII():
    while True:
        clear()
        # artList funciona como seleccionador de los asciis creo ¿?
        artList = listdir("Assets")
        # funciona igual que un for i in... pero esta ves la variable es txt, para mejor comprensión
        for txt in artList:
            # Se crea una lista
            if not txt.startswith("#"):
                artList.remove(txt)
        n = 0
        print()
        print("=" * 50)
        # Porseaca lo apunto, pero creo que el remove lo que hace es que al imprimirse solo el primero, luego se impreso se elimina y el 
        # segundo pasa a ser el primero
        for txt in artList:
            print(f"\n[{n}] [{txt[1:]}]")
            n += 1
        print()
        print("=" * 50)
        # Se muestra la segunda parte del codigo, la elección del ascii
        try:
            option = int(input("\nEscoge un ASCII Art:"))
        except ValueError:
            continue
        try:    
            path = "Assets/" + artList[option]
        except IndexError:
            continue
        print()
        # Retorna lo que el usuario quiere, por así decirlo
        return loadText(path)