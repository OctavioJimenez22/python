cadena = "Hola, mundo!"

#obtenemos la subcadena de hola [inicio:fin (sin incluirilo)]

subcadena_hola = cadena[0:4]
print(f"Subcadena de hola: {subcadena_hola}")

#se recuperan valores de la cadena principal para crear una subcadena
# colocando el nombre de la cadena y la posicion inicio seguida de dos puntos y la posicion fin

subcadena_mundo = cadena[5:12]
print(f"Subcadena mundo: {subcadena_mundo}")