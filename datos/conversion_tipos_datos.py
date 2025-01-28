# conversion de tipos de datos

#Convertir de cadena a numero
numero_cadena = "10"
numero_entero = int(numero_cadena)
print(f"Valor numerico en cadena: {numero_cadena}")
print(f"Cadena a entero: {numero_cadena}")

#Convertir de cadena a flotante
numero_cadena = "3.14"
numero_flotante= float(numero_cadena)
print(f"El vamos de numero flotante es: {numero_flotante}")

#convertir de numero a cadena
numer_entero = 25
numero_cadena = str(numer_entero)
print(f"Numero a cadena: {numero_cadena}")

#Convertir a boleano (tiene dos casos)
#El tipo booleano es Falso en los siguinetes casos:
#Si el valor es 0, caden vacia ó None, entonces regresa Falso.
#Regresa True, si el valor es distinto a Cero o a None

numero_booleano = 0
booleano = bool(numero_booleano)
print(f"El valor booleano es 0: {booleano}\n")

cadena = ""
booleano = bool(cadena)
print(f"Valor de booleano de cadena vacia = {booleano}")

cadena = "Cadena con valor"
booleano = bool(cadena)
print(f"Valor booleano de la cadena NO vacia: {booleano}")

variable = None
booleano = bool(variable)
print(f"Valor booleanos tipo None: {booleano}" )
