# vamos a usar el metodo de .find() para encontrar la posicion del incide de la subcadena
#Tener en cuenta que cuando no se encuentra el indice nos imprime como respuesta -1

cadena = "Hola mundo"
indice = cadena.find("mundo")
print(f"indice de la subcadena mundo: {indice}")

indice_hola = cadena.find("Hola")
print(f"Posicion de la subcadena hola: {indice_hola}")
