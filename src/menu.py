#
# 
# 

import os
from funcHandler import *

def clear():
    os.system("cls")


"""
Funcion que muestra visualmente las opciones disponibles
"""
def menuTexto():
    print("="*100)
    print("[1] Mostrar un ASCII ART")
    print("[2] Rotar 90 grados en sentido horario")
    print("[3] Rotar 90 grados en sentido anti-horario")
    print("[4] Rotar 180 grados en sentido horario")
    print("[5] Rotar 180 grados en sentido anti-horario")
    print("[6] Efecto espejo")
    print("[7] Frecuencias de caracteres")
    print("[0] Salir del programa")
    print("="*100)


"""
Funcion menu que recibe el input del usuario y llama a la funcion
escogida por el usuario. Permite reiniciar o no el programa.
"""
def menu():

    flag = True
    trigger = True
    while flag:
        while True:
            titulo()
            menuTexto()

            try:
                opcion = int(input("\nIngrese su opcion: "))
            except ValueError:
                clear()
                continue

            if opcion == 0:
                flag = False
                trigger = False
                break
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
                mirrorASCII()
                break
            elif opcion == 7:
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

        """
        Logica para reiniciar el programa (volver a entrar al bucle) o
        romper el bucle de reinicio y bucle de menu, finalizando el programa.       
        """
        while trigger:
            opcion = int(input("Desea volver a usar?: "))
            if opcion ==  0:
                flag = False
                break
            elif opcion == 1:
                clear()
                break
            else:
                print("Seleccione una selección valida")
    
    print("\nGracias por usar este programa.")