print("***Cajero automatico!***\n")
saldo = 1000
salir = False
 
while not salir:
    print("Operaciones que puedes realizar:\n1.Consultar saldo.\n2.Retirar.\n3.Depositar.\n4.Salir")
    opcion = int(input("\nEscoje una opción:"))
     
    if opcion == 1:
        print(f"Tu saldo actual es: ${saldo}\n")
    elif opcion == 2:
        retiro = float(input("Ingresa el monto a retirar: "))
        if saldo > retiro:
            saldo = saldo - retiro
            print(f"Tu nuevo saldo es de: ${saldo}\n")
        elif saldo < retiro:
            print(f"No cuentas con suficiente saldo. Saldo acual ${saldo}\n")
        else:
            print("Ingresa un monto correcto.")
    elif opcion == 3:
           deposito = float(input("Ingrese el valor a depositar: "))
           saldo = saldo + deposito
           print(f"Tu saldo actual es de: ${saldo}\n")
    elif opcion == 4:
        salir = True
        print("Saliendo del sistema.\nVuelve pronto!")
    else:
        print("La opción es incorrecta. Vuelve a intentarlo.")
           