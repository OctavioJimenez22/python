print("Regrasar una tupla de valores desde una funcion\n")

#definicion de la funcion
def persona_mayusculas(nombre, apellido, edad):
    print(f'Esta funcion regresa varios valores (tupla)')
    return (nombre.upper(), apellido.upper(), edad)

#programa principal
nombre, apellido, edad = persona_mayusculas('Tavo', 'Jimenez', 70)
print(f'Nombre: {nombre}, Apellido: {apellido}, Edad: {edad}')