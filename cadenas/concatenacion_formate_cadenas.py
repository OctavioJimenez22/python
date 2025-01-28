# Concatenar o unir cadenas. formatear cadenas.

cadena1 = "Hola"
cadena2 = "mundo"
cadena3= "cruel"

concatenacion1 = "Hola" + "mundo" + "cruel"
print(concatenacion1)

concatenacion2 = cadena1+" "+ cadena2+ " "+ cadena3
print(concatenacion2)

#metidi " ".join
concatenacion3 = " ".join([cadena1, cadena2, cadena3])
print(concatenacion3)

# FORMATEAR CADENAS

#Vamos a usar el metodo de f-string para este formateo de cadenas
nombre = "Tavo"
edad = 25

mensaje = f"Hola me llamo {nombre} y tengo {edad} años"
print(mensaje)

#aqui vamos con el metodo format:   recordar que para sustituir los valores de las variables
# se llena de izquierda a derecha en el .format(AQUI)
mensaje2 = "Hola me llamo {} y tengo {} años".format(nombre, edad)
print(mensaje2)
