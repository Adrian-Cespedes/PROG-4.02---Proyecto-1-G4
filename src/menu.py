from functions import *

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
    titulo()
    menuTexto()

    opcion = int(input("\nIngrese su opcion: "))

    while opcion >= 1:
        if opcion == 0:
            break
        elif opcion == 1:
            mostrarASCII()
        elif opcion == 2:
            rotar90()
        elif opcion == 3:
            rotar90Anti()
        elif opcion == 4:
            rotar180()
        elif opcion == 5:
            rotar180Anti()
        elif opcion == 6:
            frecCaracteres()
        else:
            print("Escoge una de las opciones...")
            menu()

        print()
        print("[1] SI")
        print("[0] NO")
        opcion = int(input("Desea volver a usar?: "))
        if opcion == 0:
            print("\nGracias por usar este programa.")
            quit()
        else:
            menu()
            #opcion = int(input("\nIngrese su opcion: "))