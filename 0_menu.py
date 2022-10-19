def optiones():
    print("Ingrese 1 para seleccionar 'Opcion 1'.")
    print("Ingrese 2 para seleccionar 'Opcion 2'.")
    print("Ingrese 3 para seleccionar 'Opcion 3'.")
    print("Ingrese 4 para seleccionar 'Opcion 4'.")
    print("Ingrese 5 para Salir")

def inicio():
    while True:
        optiones()
        option = int(input())
        if option == 1:
            print("----> Seleccionaste: Opcion 1")
        elif option == 2:
            print("----> Seleccionaste: Opcion 2")
        elif option == 3:
            print("----> Seleccionaste: Opcion 3")
        elif option == 4:
            print("----> Seleccionates: Opcion 4")
        elif option == 5:
            break
inicio()