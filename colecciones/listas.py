print("Manejo de listas\n")

mi_lista = [1, 2, 3, 4, 5]

print(f"{mi_lista} lista orignal")

#largo de la lista
print(f"Largo de la lista: {len(mi_lista)}")

#Acceder a los elementos de la lista por indice:
print(f"Accedemos al valor del índice 4: {mi_lista[4]}")
print(F"Accedemos al último índice de la lista: {mi_lista[-1]}")

#Modificar elementos de una lista
mi_lista[1] = 10  #cambiamos el valor 
print(F"Modificamos el valor del índice 1: {mi_lista[1]}")

#Agregar un nuevo elemento al final de la lista
mi_lista.append(6)    #metodo append() para agregar a la lista ese ultimo elemento
print(f"{mi_lista} Se agregó el elemeto 6")

#Añadir un nuevo elemento en un indice especifico
mi_lista.insert(2, 15)  #Con el metodo .insert(la posicion donde desea agregar, el valor que le quiere agregar)
print(f"{mi_lista} Se añadió el valor de 15 en el índice 2")


#Eliminar elementos de una lista
#Usando el metodo .remove(aqui el valor a eliminar)
mi_lista.remove(5)
print(f"{mi_lista}Se removi+o el valor 5")
#Usando el meotodo pop.(aqui el indice a eliminar)
mi_lista.pop(1)
print(f"{mi_lista} Se eliminó el índice 1")
#Eliminar usando la palabra del
del mi_lista[2]    # del nombre_lista[aqui el indice a eliminar]
print(f"{mi_lista} se eliminó el índice 2")


#obtener sublistas
sub_lista = mi_lista[1:3]  #Aqui tomamos la lista: nombre_lista[indice inicial:indice final] y el indice 3 no se incluye= 3-1
print(f"Esta es la sublista[1:3]: {sub_lista}")