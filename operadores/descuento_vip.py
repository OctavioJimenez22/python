no_productos_descuento = 10
cantidad_productos = int(input("Cuantos productos compraste hoy? "))
tiene_membresia = input("Tienes la membresia de la tienda (si/no)")

es_elegible_descuento = (cantidad_productos >= no_productos_descuento and tiene_membresia.strip().lower() == "si")

print(f"Tienes acceso al descuento VIP? {es_elegible_descuento}")
