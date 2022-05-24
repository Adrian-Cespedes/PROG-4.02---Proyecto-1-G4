from funcHandler import *

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
        # Crea una pequeña presentación
        titulo()
        # Esto crea lo que las instrucciones para el usuario
        menuTexto()

        opcion = int(input("\nIngrese su opcion: "))

        #Aca solo se crean condiciones según lo que ingrese el usuario
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

        # ¿Mientras sea verdad que cosa?¿Flag?
        while True:
            # Le pregunta al ususariosi desea volver a usa
            opcion = int(input("Desea volver a usar?: "))
            if opcion ==  0:
                flag = False
                # ¿Y por eso lo anterior no?¿Pero esto no debería de ir más arriba?
                break
            elif opcion == 1:
                break
            else:
                print("Seleccione una selección valida")
    
    print("\nGracias por usar este programa.")