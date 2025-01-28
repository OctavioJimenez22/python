#Metodos utiles para las cadenas

cadena1 = "Hola Mundo"

print(f"Cadena origina {cadena1}")

#Vamos a pasar a mayusculas con el metodo .upper()
mayusculas = cadena1.upper()
print(f"Cadena en mayusculas: {mayusculas}")

#Vamos a pasar a minusculas con el metodo .lower() pero directamente lo cual se puede con el .upper()
print(f"Cadena en minusculas: {cadena1.lower()}")

#Vamos a cortar los espacios en blanco con el metodo .strip()
print()
cadena2 = " Tavo Jimenez "
print(f"Cadena con espacios:{cadena2}.")
print(f"Cadena sin espacios al principio y al final:{cadena2.strip()}.")