from os import listdir, system
from functions.imports.loader import loadText
from functions.randomScrap import randomScrap

def clear():
    system("cls")

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
        # Porseaca lo apunto, pero creo que el remove lo que hace es que al imprimirse solo el primero, luego se impreso se elimina y el 
        # segundo pasa a ser el primero
        for txt in artList:
            print(f"\n[{n}] [{txt[1:]}]")
            n += 1
        print(f"\n[{n}] Web Scraping...")
        print()
        print("=" * 50)
        try:
            option = int(input("\nEscoge un ASCII Art:"))
        except ValueError:
            continue
        if option < len(artList):  
            path = "Assets/" + artList[option]
            print()
            return loadText(path)
        elif option == n:
            return randomScrap()
        else:
            continue