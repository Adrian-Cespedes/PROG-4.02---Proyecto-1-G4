from os import listdir
from functions.imports.loader import loadText

def selectASCII():
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
    option = int(input("\nEscoge un ASCII Art:"))
    while not option < len(artList):
        n = 0
        print()
        print("=" * 50)
        for txt in artList:
            print(f"\n[{n}] [{txt[1:]}]")
            n += 1
        print()
        print("=" * 50)
        option = int(input("\nEscoge un ASCII Art:"))
    path = "Assets/" + artList[option]
    print()
    return loadText(path)