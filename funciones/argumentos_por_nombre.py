print("Funcion argumentos por nombre\n")

def imprimir_persona(nombre, apellido, edad):
    print(f'Nombre: {nombre}, Apellido: {apellido}, Edad: {edad}')
    

#Llamamos la funcion pasando los agumentos de manera posicional
imprimir_persona('Tavo', 'Jimenez', 26)
print (imprimir_persona)
imprimir_persona(nombre='Patricia', apellido = 'Jimenez', edad = 60)
print(imprimir_persona)

#argumentos con valores por default
imprimir_persona(nombre='Tavo', apellido='Jimenez')
print(imprimir_persona)