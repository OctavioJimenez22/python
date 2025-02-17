print("Bienvenido a tu Playlist!")

lista_canciones = []
numero_canciones = int(input("Cuantas canciones quiere agregar a la playlist: "))

for i in range(numero_canciones):
    cancion = input(f"Proporciona la cancion {i + 1}:")
    lista_canciones.append(cancion)

print("\nLista de canciones: ")
sonar = None
posicion = 1
for sonar in lista_canciones:
    print(f"{posicion}.",sonar)
    posicion +=1