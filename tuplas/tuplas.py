print("**Manejo de Tuplas***\n")

mi_tupla = (1, 2, 3, 4, 5)
print(mi_tupla)
#En tuplas no se pueden modificar los elementos.

for elemento in mi_tupla:
    print(elemento,end=" ")

#Creamos una tupla para una cordenada de x, y
coordenadas = (3, 5)
print(f"\nCoordenada en el eje x: {coordenadas[0]}")
print(f"Coordenada en el eje y: {coordenadas[1]}")

#Crear una tupla unitaria
tupla_un_elemento = 10,    #Le agregamos la como para que se entienda que es una tupla_un_elemento
print(f"La tupla de un elemento: {tupla_un_elemento}")

#Tupla anidada. Tupla de tuplas
tuplas_anidada = (1, (2,3), (4, 5))
print(f"Segundo elemento de la tupla anidada: {tuplas_anidada[1]}")