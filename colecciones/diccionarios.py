print("Diccinarios en Python\n")

personas = {
    'nombre': 'Tavo',
    'edad': 26,
    'cuidad': 'Medellin'
}

print(f'Diccionairo de persona: {personas}')

#Accerder a los elementos del diccionario
print(f'Nombre: {personas['nombre']}')
print(f'Cuidad: {personas['cuidad']}')
print(f'Edad: {personas['edad']}')

#modificar un valor del diccionario
personas['edad'] = 25
print(f'Edad modificadda: {personas['edad']}')

#Agregar un nuevo elemento al diccionario
personas['color_favorito'] = 'Negro'
print(f'Color favorito: {personas['color_favorito']}')

#Eliminar un elemento del diccionario
del personas['color_favorito']
print(f'Eliminamos el color favorito: {personas}')
personas.pop('edad')
print(f'Eliminamos la edad: {personas}')

#Iteramos los elementos de un dict (llave, valor)
print(f'\nValores del diccionario')
for llave, valor in personas.items():
    print(f'Llave: {llave}, Valor: {valor}')

#obtener cada una de las llaves
print(f'\nImprimir solo las llaves: ')
for llave in personas.keys():
    print(llave)

