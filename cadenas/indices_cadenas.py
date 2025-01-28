# Manejo de indices en una cadena

cadena1 = "Hola Mundo"
print(cadena1)

# Recuperar el primer caracter

primer_Caracter = cadena1[0]
print(primer_Caracter)

ultimo_Caracter = cadena1[9]
print(ultimo_Caracter)

# Inmutabilidad en cadenas
# Esa cadena inicial asi entre comillas, NO PUEDE SER MODIFICADA
# solo se puede hacer de la siguiente manera:

cadena1 = "Hola mundo"
Cadena2 = cadena1
cadena1 = "Adios"
print()
print(cadena1)
print(Cadena2)
#lo unico que estamos haciendo es guardar los valores de la cadena1 en la 2 para no perder los datos
