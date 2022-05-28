import os
from funcHandler import *

# Funcion para limpiar la consola
def clear():
    os.system("cls")

#Decoración principal
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

# Flag nos sirve como un booleano
    flag = True
    while flag:
        # While anidado para controlar opciones no validas y reiniciar las opciones
        while True:
            # Crea una pequeña presentación
            titulo()
            # Esto crea lo que las instrucciones para el usuario
            menuTexto()

            # Handling Exception si opcion no es int
            try:
                opcion = int(input("\nIngrese su opcion: "))
            except ValueError:
                clear()
                continue

            # Opciones disponibles
            if opcion == 0:
                flag = False
            elif opcion == 1:
                clear()
                showASCII()
                break
            elif opcion == 2:
                clear()
                rotate90()
                break
            elif opcion == 3:
                clear()
                rotate90Anti()
                break
            elif opcion == 4:
                clear()
                rotate180()
                break
            elif opcion == 5:
                clear()
                rotate180Anti()
                break
            elif opcion == 6:
                clear()
                frecChars()
                break
            else:
                print("Escoge una de las opciones...")
                clear()
                continue

        print()
        print("[1] SI")
        print("[0] NO")

        # While anidado para poder "reiniciar" y volver al while principal si se desea volver a usar
        while True:
            # Le pregunta al ususariosi desea volver a usa
            opcion = int(input("Desea volver a usar?: "))
            if opcion ==  0:
                flag = False
                # Romper todo el while, cerrando el programa
                break
            elif opcion == 1:
                clear()
                break
            else:
                print("Seleccione una selección valida")
    
    print("\nGracias por usar este programa.")