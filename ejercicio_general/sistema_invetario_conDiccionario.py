print('Sistemas de inventarios\n')

agregar_productos = input('Cuantos productos desea agregar?: ')

inventario = []

for i in range(int(agregar_productos)):
    nombre = input('Ingrese el nombre del producto: ')
    precio = float(input('Ingrese el precio del producto: '))
    cantidad = int(input('Ingrese la cantidad del producto: '))

    producto = {'indice': i+1, 'nombre': nombre, 'precio': precio, 'cantidad': cantidad}
    inventario.append(producto)
    
print(f'\nInventario de productos: {inventario}\n')

#Buscar un producto
id_buscar = int(input('Ingrese el indice del producto a buscar: '))
for producto in inventario:
    if producto.get('indice') == id_buscar:
        print(f'Producto encontrado: {producto}')
        break

