
compra = int(input("Monto de tu compra:"))
miembro = input("Eres miembro (si/no)")
descuento = 0

if compra >= 1000 and miembro.strip().lower() == "si":
    print(f"\nTu {miembro} y tu compra es de {compra} entonces tu descuento es de 10%")
    descuento = compra * 0.10
elif compra < 1000 and miembro.strip().lower() == "si":
    print(f"\nNo tienes mas de $1000 en monto de compara pero tu {miembro} eres miembro entonces tienes descuento del 5%")
    descuento = compra * 0.05
elif compra >= 1000 and miembro.strip().lower() == "no":
    print(f"Monto mayor a $1000 pero tu {miembro} eres miembro. Tu descuento es del 3%")
    descuento = compra * 0.03
else:
    print(f"\nTu {miembro} miembro y tienes 0% de descuento\nTe invitamos a ser miembro de la tienda")
    descuento = 0

monto_final = compra - descuento

print(f"El monto de tu compra es de: ${compra:.2f}")
print(f"Monto de descuento es de ${descuento:.0f}")
print(f"El monto final de la compra es de: {monto_final:.2f}%")