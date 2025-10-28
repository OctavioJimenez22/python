print("Operaciones con Set\n")

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

union = a | b
print(f"Union a | b: {union}")

interseccion = a & b    #Solo los valores que son iguales en los conjuntos
print(f"Intersección a & b: {interseccion} ")  

diferencia = a - b #Los elementos que se repiten en los conjuntos se eliminan en el primero y se imprime el primer conjunto
print(f"Diferencia a- b: {diferencia}")

