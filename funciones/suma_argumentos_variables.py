print('Suma con argumentos variables')

#Funcion sumar que acepta argumentos variables
def sumar(*args):
    total = 0
    for numero in args:
        total += numero
    return total
#llamamos la funcion sumar
resulado1 = sumar(1, 2, 3, 4, 5)
print(f'Resultado de la suma: {resulado1}')