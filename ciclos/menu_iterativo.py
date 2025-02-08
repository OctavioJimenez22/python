salir = False

while not salir:
    print(f"Menu:\n1.Crear cuenta.\n2.Eliminar cuenta.\n3.Salir")
    opcion = int(input("Escoje una opción: "))
    if opcion == 1:
        print("Creando tu cuenta...\n")
    elif opcion == 2:
        print("Eliminando tu cuenta...\n")
    elif opcion == 3:
        print("Saliendo del sistema. Hasta pronto.\n")
        salir = True
    else:
        print("Opción inválida. Elije otra opción")
else:
    print("Terminando el sistema de administración de cuentas.")