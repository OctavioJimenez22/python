print("**CALCULADORA\n")

opcion = a = b = total = 0
salir = False

while not salir:
    print('''Posibles opciones:
    1.Suma.
    2.Resta.
    3.Multiplicación.
    4.División.
    5.Salir.''')
    
    opcion = int(input("Escoje una opción: "))
    
    if opcion == 1:
        a = float(input("Ingrese el primer valor: "))
        b = float(input("Ingrese el segundo valor: "))
        total = a + b
        print(f"El total de la suma es de: {total}")
    elif opcion ==2:
        a = float(input("Ingrese el primer valor: "))
        b = float(input("Ingrese el segundo valor: "))
        total = a - b
        print(f"El total de la resta es de: {total}")
    elif opcion ==3:
        a = float(input("Ingrese el primer valor: "))
        b = float(input("Ingrese el segundo valor: "))
        total = a * b
        print(f"El total de la multiplicación es de: {total}")    
    elif opcion ==4:
        a = float(input("Ingrese el primer valor: "))
        b = float(input("Ingrese el segundo valor: "))
        total = a / b 
        print(f"El total de la división es de: {total}")
    elif opcion == 5:
        print("Saliendo de la calculadora...\nVuelve pronto!")    
        salir = True       
    else:
        print("Opción invalida!\nVuelve a intentarlo")