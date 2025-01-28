#Asignacion multiple:
nombre, apellido, color = "Tavo", "Jimenez", "Azul"
print(nombre,apellido,color)

#asignacion en cadena:
variable_1 = varible_2 = 0
print(variable_1, varible_2)

#Intercambio de una variable, sin utilizar variables temporales
x, y = 5, 10
print(f"Valor principal de x = {x}, valor original de y= {y}")
#aplicando el concepto  de asignacion multiple, intercanbiamos valores:
x, y = y, x
print(f"Valor cambiado de x = {x}, valor cambiado de y = {y}\n")

# recibir multiples valores de la entrada del usuario:

nombre, apellido = input("Ingres el nombre y apellido separados por coma: ").split(",")

print(f"Nombre: {nombre.strip()}, apellido: {apellido.strip()}")