from funcHandler import *

def menuTexto():
    print("="*100)
    print("[1] Mostrar un ASCII ART")
    print("[2] Rotar 90 grados en sentido horario")
    print("[3] Rotar 90 grados en sentido anti-horario")
    print("[4] Rotar 180 grados en sentido horario")
    print("[5] Rotar 180 grados en sentido anti-horario")
    print("[6] Frecuencias de caracteres")
    print("[0] Salir del programa")
    print("="*100)

def menu():

    flag = True
    while flag:
        titulo()
        menuTexto()

        opcion = int(input("\nIngrese su opcion: "))

        if opcion == 0:
            break
        elif opcion == 1:
            showASCII()
        elif opcion == 2:
            rotate90()
        elif opcion == 3:
            rotate90Anti()
        elif opcion == 4:
            rotate180()
        elif opcion == 5:
            rotate180Anti()
        elif opcion == 6:
            frecChars()
        else:
            print("Escoge una de las opciones...")

        print()
        print("[1] SI")
        print("[0] NO")

        while True:
            opcion = int(input("Desea volver a usar?: "))
            if opcion ==  0:
                flag = False
                break
            elif opcion == 1:
                break
            else:
                print("Seleccione una selección valida")
    
    print("\nGracias por usar este programa.")