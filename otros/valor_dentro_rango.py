VALOR_MINIMO = 0
VALOR_MAXIMO = 5

valor_ingresado = int(input(f"Ingrese el valor entre {VALOR_MINIMO}y{VALOR_MAXIMO}: "))

#comprobamos si el valor ingresado esta dentro de 0 y 5
comprobante = valor_ingresado >= VALOR_MINIMO and valor_ingresado <= VALOR_MAXIMO
print(f"El valor ingresado dentro del rango es: {comprobante}")

