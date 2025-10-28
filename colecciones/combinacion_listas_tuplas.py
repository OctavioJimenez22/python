print("Combinación de Tistas y Tuplas")

productos = [
    ("P001", "Camisa", 20.00),
    ("P002", "Jeans", 30.00),
    ("P003", "Sudadera", 40.00),
]

#Imprimir la información de cada producto
#Y calculamos el precio total
precio_total = 0

print("Información de los productos:\n")
for producto in productos:
    id, descripcion, precio = producto  #unpacking- desempaquetado
    print(f"Id: {id},Descripción: {descripcion} ,Precio: {precio}")
    precio_total += precio  #producto[2]
print(f"\nPrecio total de los productos: {precio_total}")

