precio_leche = float(input("Precio leche: "))
precio_pan = float(input("Precio pan: "))
precio_lechuga = float(input("Precio lechuga: "))
precio_platanos = float(input("Precio platanos: "))
descuento_porcentaje = int(input("Aplicar algun descuento (%)? "))


#calculamos el subtotal
subtotal = precio_leche + precio_pan + precio_lechuga + precio_platanos

#aplicar descuento
descuento = subtotal * (descuento_porcentaje/100)

#subtotal con descuento
subtotal_descuento = subtotal - descuento

#Calculo con impuestos (16%)
impuesto = subtotal_descuento * 0.16

#calculo total de la compra
costo_total_compra = subtotal_descuento + impuesto

print(f"Subtotal: ${subtotal:.2f}\n Descuento: ${descuento}\nSubtotal con descuento: ${subtotal_descuento}")
print(F"Impuestos (16%): {impuesto:.2f}\nCosto total de la compra: ${costo_total_compra:.2f}")

 