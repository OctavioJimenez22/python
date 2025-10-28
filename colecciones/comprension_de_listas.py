print('Compresion de listas\n')

numeros = [1,2,3,4,5,6,7,8,9,10]
cuadrado = [x**2 for x in numeros]
print(f'Numeros: {numeros}')
print(f'Cuadrados: {cuadrado}')

#Lista de numeros pares
numero = (10+1)
pares = [x for x in range(numero) if x % 2 == 0]
print(f'Numeros pares hasta el {numero}: {pares}')

#lista saludando a cada nombre
nombres = ['Tavo', 'Maria', 'Carlos']
saludando = [f'Hola {nombres}' for nombres in nombres]
print(f'Saludando: {saludando}')