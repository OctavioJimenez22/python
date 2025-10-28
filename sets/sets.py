print("Manejo de Sets\n")

#Para los sets no tienen orden, no tienen indice y se eliminan o ignoran los elementos duplicados.

mi_set = {1,2,3,4,5,4}

print(f"Mi Set: {mi_set}")

#Agregar elementos al Set:
mi_set.add(6)
mi_set.add(7)
print(f"Set modificado: {mi_set}")

#Intentamos agregar un elemento agregado:
mi_set.add(3)
print(f"Set modificado: {mi_set}")

#Para eliminar un elemento del conjunto:
mi_set.remove(3)
print(f"Set modificado: {mi_set}")

#Iterar los elementos del Set:
for elemento in mi_set:
    print(elemento, end=" ")
    
#Comprobar si existe un elemento en el set:
print(f"\Existe el valor de 4 en el Set: {4 in mi_set}")
print(f"\Existe el valor de 10 en el Set: {10 in mi_set}")

#obtener la longitud del Set:
print(f"Longitud del conjutno: {len(mi_set)}")