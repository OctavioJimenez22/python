print("Contador de vocales\n")

cadena = "Hola Mundo"
cantidad = 0

for i in range(len(cadena)):
    if cadena[i].lower() in "aeiou":
        cantidad +=1
        print(cadena[i])
print(f"\nLa canditdad de vocales es: {cantidad}")
        
        
