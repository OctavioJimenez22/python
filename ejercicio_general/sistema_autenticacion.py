#crear 2 constantes para definir valores correctos para luego comparar
#solicitar el usuario y la contraseña y si son iguales que los valores correctos almacenas
#en las constantes debe imprimir True 

NOMBRE = "tavo"
CONTRASEÑA = "hola123"

nombre = input("Usuario: ")
Contraseña = input("Contraseña: ")

correcto = NOMBRE == nombre and CONTRASEÑA == Contraseña
print(f"Datos correctos?: {correcto}")
 