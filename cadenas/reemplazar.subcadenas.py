# usamos el metodo .replace() para reemplazar subcadenas de la cadena principal

cadena = "Hola, mundo!"
nueva_subcadena = cadena.replace("mundo", "Tavo")
print(f"Cadena original: {cadena}")
print(f"cadena reemplazada: {nueva_subcadena}") 

nueva_subcadena_adios = nueva_subcadena.replace("Tavo", "adios!")
print(f"Otro reemplazo: {nueva_subcadena_adios}")