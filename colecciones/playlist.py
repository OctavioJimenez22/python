print("Playlist de canciones\n")

lista_reproduccion = []

lista_reproduccion.append("Hotel California.")
lista_reproduccion.append("Staying Alive.")
lista_reproduccion.append("Dream on.")

lista_reproduccion.sort()  #El metodo .sort() es para ordenar de forma ascendente los elementos de la lista
print("Lista de forma ascendente:\n",lista_reproduccion)

lista_reproduccion.sort(reverse = True) #Para orderna la lista de forma descendente
print("Lista de forma desecente:\n", lista_reproduccion)


print("\nLista de canciones:")
posicion = 1
for cancion in lista_reproduccion:
    print(f"{posicion}.", cancion)
    posicion +=1